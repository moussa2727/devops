terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
  host = "unix:///var/run/docker.sock"
}

# On utilise l'image déjà buildée par Jenkins
resource "docker_container" "openrecon_container" {
  name  = "openrecon-service"
  image = "openrecon-app:latest"

  ports {
    internal = 5000
    external = 8081
  }

  restart = "always"
  must_run = true
}
