resource "aws_security_group" "app" {
  name_prefix = "${var.environment}-app-"
  description = "Security group for the Flask application"
  vpc_id      = aws_vpc.lab.id

  tags = {
    Name        = "${var.environment}-app-sg"
    Environment = var.environment
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_vpc_security_group_ingress_rule" "app" {
  security_group_id = aws_security_group.app.id
  description       = "Application access from approved CIDR"
  cidr_ipv4         = var.allowed_app_cidr
  from_port         = var.app_port
  to_port           = var.app_port
  ip_protocol       = "tcp"
}

resource "aws_vpc_security_group_egress_rule" "app" {
  security_group_id = aws_security_group.app.id
  description       = "Application outbound access"
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "-1"
}

resource "aws_security_group" "database" {
  name_prefix = "${var.environment}-database-"
  description = "Security group for PostgreSQL"
  vpc_id      = aws_vpc.lab.id

  tags = {
    Name        = "${var.environment}-database-sg"
    Environment = var.environment
  }

  lifecycle {
    create_before_destroy = true
  }
}

resource "aws_vpc_security_group_ingress_rule" "database_from_app" {
  security_group_id            = aws_security_group.database.id
  referenced_security_group_id = aws_security_group.app.id
  description                  = "PostgreSQL access from application SG"
  from_port                    = 5432
  to_port                      = 5432
  ip_protocol                  = "tcp"
}

resource "aws_vpc_security_group_egress_rule" "database" {
  security_group_id = aws_security_group.database.id
  description       = "Database outbound access for this lab"
  cidr_ipv4         = "0.0.0.0/0"
  ip_protocol       = "-1"
}