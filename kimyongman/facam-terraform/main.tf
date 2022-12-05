
locals {
  common_tags = {
    Environment = "dev"
    Application = "myapp"
    Terraform   = "true"
  }
}

resource "aws_instance" "ec2_example" {
  ami           = data.aws_ami.amazon_linux2.id
  instance_type = "t2.micro"
  tags = {
    Name = "fastcampus-tf-ec2-example"
  }
}