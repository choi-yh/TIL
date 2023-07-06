# terraform block - terraform settings
# 각 provider 는 source 옵션을 통해 정의하며,
# hostname, namespace, provider type 등을 정의 할 수 있다.
terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

# provider block - define provider
variable "google_application_credentials" {
  default = ""
}
variable "gcp_project" {
  default = ""
}
provider "google" {
  credentials = file(var.google_application_credentials)

  project = var.gcp_project
  region  = "us-central1"
  zone    = "us-central1-c"
}

# resource blocks - define components of my infrastructure
# resource block 에는 두가지 string 이 있어야 한다. (resource type, resource name)
# `google_compute_network.vpc_network`
resource "google_compute_network" "vpc_network" {
  name = "dante-terraform-network"
}

# boot_disk, network_interface 같은 추가 파라미터는
# https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/compute_instance?product_intent=terraform
# 에서 확인 가능하다.
resource "google_compute_instance" "vm_instance" {
  machine_type = "f1-micro"
  name         = "dante-terraform-instance"
  tags         = ["web", "dev", "dante"]

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-11"
    }
  }

  network_interface {
    network = google_compute_network.vpc_network.name
    access_config {}
  }
}
