terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

# Gestion de l'image (détruit l'ancienne si mise à jour)
resource "docker_image" "myapp_image" {
  name         = "devops-app:latest"
  keep_locally = false 
}

# Gestion du conteneur
resource "docker_container" "myapp_container" {
  image = docker_image.myapp_image.image_id
  name  = "mon_conteneur_app"
  
  ports {
    internal = 5000 # Port interne Flask
    external = 8081 # Port d'accès sur ta machine (port 8081)
  }

  restart = "on-failure"
}
