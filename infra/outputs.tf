
output "container_name" {
  description = "Name of the Server Sentinel container"
  value       = docker_container.server_sentinel.name
}

output "application_url" {
  description = "Local URL for Server Sentinel"
  value       = "http://localhost:8000"
}

output "container_id" {
  description = "Docker container ID"
  value       = docker_container.server_sentinel.id
}
