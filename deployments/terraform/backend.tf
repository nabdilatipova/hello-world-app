terraform {
  backend "gcs" {
    bucket  = "nasyikat-fuchicorp"
    prefix  = "dev/hello-world"
    project = "mineral-order-315523"
  }
}
