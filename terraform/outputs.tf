output "vpc_id" {
  description = "ID of the lab VPC"
  value       = aws_vpc.lab.id
}

output "public_subnet_id" {
  description = "ID of the public subnet"
  value       = aws_subnet.public.id
}

output "instance_id" {
  description = "ID of the EC2 web server"
  value       = aws_instance.web.id
}

output "public_ip" {
  description = "Public IP address of the EC2 web server"
  value       = aws_instance.web.public_ip
}

output "website_url" {
  description = "URL of the lab website"
  value       = "http://${aws_instance.web.public_ip}"
}