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
        image = "hashicorp/http-echo:0.2.3"
        args  = ["-text=Hello, DevOps!"]
      }

      resources {
        cpu    = 100
        memory = 64
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
