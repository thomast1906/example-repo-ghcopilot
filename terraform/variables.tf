variable "location" {
  description = "The Azure region to deploy resources to"
  type        = string
  default     = "uksouth"
}

variable "environment" {
  description = "Environment name (e.g. dev, prod)"
  type        = string
}

variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
}

variable "app_name" {
  description = "Name of the application"
  type        = string
  default     = "flask-web-app"
}

variable "tags" {
  description = "Tags to apply to all resources"
  type        = map(string)
  default     = {
    Application = "Flask Web App"
    Environment = "Development"
    ManagedBy   = "Terraform"
  }
}