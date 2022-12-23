module "iam_assumable_role_ebs_controller" {
  source                        = "terraform-aws-modules/iam/aws//modules/iam-assumable-role-with-oidc"
  version                       = "5.3.1"
  create_role                   = true
  role_name                     = "${local.cluster_name}-eks-ebs-csi-driver-role"
  role_description              = "Used by EBS CSI DRIVER for EKS"
  provider_url                  = module.eks.cluster_oidc_issuer_url
  oidc_fully_qualified_subjects = ["system:serviceaccount:kube-system:ebs-csi-controller-sa"]
}

data "aws_iam_policy" "aws_ebs_csi_driver_policy" {
  arn = "arn:aws:iam::aws:policy/service-role/AmazonEBSCSIDriverPolicy"
}

resource "aws_iam_role_policy_attachment" "ebs_controller_policy" {
  role       = module.iam_assumable_role_ebs_controller.iam_role_name
  policy_arn = data.aws_iam_policy.aws_ebs_csi_driver_policy.arn
}