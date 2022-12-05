terraform {
  backend "s3" {
    bucket         = "fastcampus-my-terraform"
    dynamodb_table = "fastcampus-my-dynamodb-state-lock"
    encrypt        = true
    key            = "remote"
    region         = "ap-northeast-2"
  }
}
