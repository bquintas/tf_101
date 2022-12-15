terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "eu-west-1"
}

resource "aws_instance" "app_server" {
  ami                    = "ami-01cae1550c0adea9c"
  instance_type          = var.instance_type
  vpc_security_group_ids = ["sg-0a7f735dd323cdf14"]
  subnet_id              = "subnet-0764f14532b83858b"

  tags = {
    Name = "ExampleAppServerInstance"
  }
}
