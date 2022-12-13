locals {
  cluster_name    = var.cluster_name
  cluster_version = var.cluster_version
  region          = "ap-northeast-2"
  vpc_id          = var.vpc_id
  public_subnets  = var.public_subnets
  private_subnets = var.private_subnets

  tag = {
    Environment = "test"
    Terraform   = "true"
  }
}

module "eks" {
  # https://registry.terraform.io/modules/terraform-aws-modules/eks/aws/latest
  source  = "terraform-aws-modules/eks/aws"
  version = "18.29.0"

  # Cluster Name Setting
  cluster_name    = local.cluster_name
  cluster_version = local.cluster_version

  # Cluster Endpoint Setting
  cluster_endpoint_private_access = true
  cluster_endpoint_public_access  = true

  # IRSA Enable / OIDC 구성
  enable_irsa = true

  # Network Setting
  vpc_id     = local.vpc_id
  subnet_ids = local.private_subnets

  # Cluster Logging Setting
  cluster_enabled_log_types = ["api"]

  # Extend node-to-node security group rules
  node_security_group_additional_rules = {
    ingress_self_all = {
      description = "Node to node all ports/protocols"
      protocol    = "-1"
      from_port   = 0
      to_port     = 0
      type        = "ingress"
      self        = true
    }
    egress_all = {
      description      = "Node all egress"
      protocol         = "-1"
      from_port        = 0
      to_port          = 0
      type             = "egress"
      cidr_blocks      = ["0.0.0.0/0"]
      ipv6_cidr_blocks = ["::/0"]
    }
    ingress_allow_access_from_control_plane = {
      type                          = "ingress"
      protocol                      = "tcp"
      from_port                     = 9443
      to_port                       = 9443
      source_cluster_security_group = true
      description                   = "Allow access from control plane to webhook port of AWS load balancer controller"
    }
    ingress_allow_access_for_metric_server = {
      type                          = "ingress"
      protocol                      = "tcp"
      from_port                     = 4443
      to_port                       = 4443
      source_cluster_security_group = true
      description                   = "Allow access from control plane to worker for metric-server apiservice"
    }
    ingress_nodes_karpenter_port = {
      description                   = "Cluster API to Node group for Karpenter webhook"
      protocol                      = "tcp"
      from_port                     = 8443
      to_port                       = 8443
      type                          = "ingress"
      source_cluster_security_group = true
    }
  }

  eks_managed_node_groups = {
    initial_node = {
      instance_types        = ["t3.large"]
      create_security_group = false

      min_size     = 2
      max_size     = 3
      desired_size = 2

      iam_role_additional_policies = [
        "arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore"
      ]
    }
  }

  # Extend cluster security group rules
  cluster_security_group_additional_rules = {
    egress_nodes_ephemeral_ports_tcp = {
      description                = "To node 1025-65535"
      protocol                   = "tcp"
      from_port                  = 1025
      to_port                    = 65535
      type                       = "egress"
      source_node_security_group = true
    }
  }

  create_aws_auth_configmap = true
  manage_aws_auth_configmap = true

  # console identity mapping (AWS user)
  # eks configmap aws-auth에 콘솔 사용자 혹은 역할을 등록
  aws_auth_users = [
    {
      userarn  = "arn:aws:iam::<AWS 어카운트 ID>:user/admin"
      username = "admin"
      groups   = ["system:masters"]
    },
  ]

  aws_auth_accounts = [
    "<AWS 어카운트 ID>"
  ]
}

resource "aws_security_group_rule" "cluster_inbound_rule" {
  type              = "ingress"
  from_port         = 30000
  to_port           = 32767
  protocol          = "tcp"
  cidr_blocks       = ["10.0.0.0/16"]
  security_group_id = module.eks.cluster_primary_security_group_id
}

// 프라이빗 서브넷 태그
resource "aws_ec2_tag" "private_subnet_tag" {
  for_each    = toset(local.private_subnets)
  resource_id = each.value
  key         = "kubernetes.io/role/internal-elb"
  value       = "1"
}

resource "aws_ec2_tag" "private_subnet_cluster_tag" {
  for_each    = toset(local.private_subnets)
  resource_id = each.value
  key         = "kubernetes.io/cluster/${local.cluster_name}"
  value       = "owned"
}

// 퍼블릭 서브넷 태그
resource "aws_ec2_tag" "public_subnet_tag" {
for_each    = toset(local.public_subnets)
resource_id = each.value
key         = "kubernetes.io/role/elb"
value       = "1"
}

resource "aws_ec2_tag" "public_subnet_cluster_tag" {
for_each    = toset(local.public_subnets)
resource_id = each.value
key         = "kubernetes.io/cluster/${local.cluster_name}"
value       = "owned"
}
