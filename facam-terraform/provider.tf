provider "aws" {

  region  = "ap-northeast-2"
  profile = "facam"

  access_key = ""
  secret_key = ""

  default_tags {
    tags = local.common_tags
  }
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.0"
    }
  }
}

