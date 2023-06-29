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
  name = "terraform-network"
}
