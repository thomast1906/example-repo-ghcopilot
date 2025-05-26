# Backend configuration for Terraform state management
# Uses Azure Storage Account for secure and collaborative state management
# Note: Replace placeholders with actual values before use

terraform {
  backend "azurerm" {
    resource_group_name  = "terraform-state-rg"
    storage_account_name = "tfstateaccountxxxxx"
    container_name       = "tfstate"
    key                  = "flask-app.tfstate"
  }
}