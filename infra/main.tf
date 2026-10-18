
resource "docker_container" "server_sentinel" {
  name  = "server-sentinel"
  image = "sha256:7b86280be2de"

  ports {
    internal = 8000
    external = 8000
  }

  volumes {
    host_path      = abspath("${path.module}/../data")
    container_path = "/app/data"
  }
}
