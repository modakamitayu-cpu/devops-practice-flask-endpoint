variable "aws_region" {
  description = "AWS Region used for lab"
  type        = string
  default     = "ap-south-1"
}

variable "environment" {
  description = "Deployment Environment"
  type        = string
  default     = "dev"

  validation {
    condition     = contains(["dev", "stage", "prod"], var.environment)
    error_message = "Environment must be dev, stage, or Prod"
  }
}

variable "vpc_cidr" {
  description = "CIDR block for the VPC"
  type        = string
  default     = "10.20.0.0/16"

  validation {
    condition     = can(cidrnetmask(var.vpc_cidr))
    error_message = "vpc_CIDR must be a valid IPv4 CIDR"
  }

}

variable "public_subnet_cidr" {
  description = "CIDR block for the public subnet"
  type        = string
  default     = "10.20.1.0/24"

}

variable "private_subnet_cidr" {
  description = "CIDR block for the private subnet"
  type        = string
  default     = "10.20.2.0/24"
}

variable "availability_zone" {
  description = "subnet Availability Zone for single-AZ lab"
  type        = string
  default     = "ap-aouth-1a"
}

variable "app_port" {
  description = "Application Listener Port"
  type        = string
  default     = "8000"

  validation {
    condition     = var.app_port >= 1 && var.app_port <= 65535
    error_message = "App port must be between 1 and 65535"
  }
}

variable "allowed_app_cidr" {
  description = "CIDR permitted to reach the application"
  type        = string
  default     = "127.0.0.1/32"

  validation {
    condition     = can(cidrnetmask(var.allowed_app_cidr))
    error_message = "allowed_app_cidr must be a valid IPv4 CIDR."
  }

}