locals {
  tags = {
    Environment = "test"
    Terraform   = "true"
  }
}

resource "aws_iam_user" "github-action" {
  name = "github-action"
  tags = local.tags
}

resource "aws_iam_user_policy" "github-action-pol" {
  name = "github-action-pol"
  user = aws_iam_user.github-action.name

  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AllowPush",
            "Effect": "Allow",
            "Action": [
                "ecr:GetDownloadUrlForLayer",
                "ecr:BatchGetImage",
                "ecr:BatchCheckLayerAvailability",
                "ecr:PutImage",
                "ecr:InitiateLayerUpload",
                "ecr:UploadLayerPart",
                "ecr:CompleteLayerUpload"
            ],
            "Resource": "arn:aws:ecr:ap-northeast-2:${data.aws_caller_identity.current.account_id}:repository/fastc-app"
        },
        {
            "Sid": "GetAuthorizationToken",
            "Effect": "Allow",
            "Action": [
                "ecr:GetAuthorizationToken"
            ],
            "Resource": "*"
        }
    ]
}
EOF
}