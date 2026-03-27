job "hello-devops" {
  datacenters = ["dc1"]
  type        = "service"

  group "app" {
    count = 1

    network {
      mode = "bridge"
    }

    task "hello" {
      driver = "docker"

      config {
        image = "hello-devops:latest"
      }

      resources {
        cpu    = 100  # MHz
        memory = 64   # MB
      }

      restart {
        attempts = 2
        interval = "1m"
        delay    = "10s"
        mode     = "fail"
      }
    }
  }
}
