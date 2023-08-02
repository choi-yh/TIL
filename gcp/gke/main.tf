terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

# provider block - define provider
provider "google" {
  credentials = file(var.google_application_credentials)

  project = var.gcp_project
  region  = var.region
  zone    = var.zone
}


resource "google_service_account" "default" {
  account_id = var.google_service_account
}

resource "google_container_cluster" "primary" {
  name = "dante-tf-gke-cluster"

  remove_default_node_pool = true
  initial_node_count       = 3

  node_config {
    machine_type = "e2-small"

    # Google recommends custom service accounts that have cloud-platform scope and permissions granted via IAM Roles.
    service_account = google_service_account.default.email
    oauth_scopes    = [
      "https://www.googleapis.com/auth/cloud-platform"
    ]

    tags = ["dante"]
  }
}
