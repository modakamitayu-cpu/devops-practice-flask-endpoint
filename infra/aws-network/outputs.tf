output "vpc_id" {
  description = "ID of the lab VPC"
  value       = aws_vpc.lab.id
}

output "public_subnet_id" {
  description = "ID of the public subnet"
  value       = aws_subnet.public.id
}

output "private_subnet_id" {
  description = "ID of the private subnet"
  value       = aws_subnet.private.id
}

output "app_security_group_id" {
  description = "Security group assigned to the application"
  value       = aws_security_group.app.id
}

output "database_security_group_id" {
  description = "Security group assigned to PostgreSQL"
  value       = aws_security_group.database.id
}