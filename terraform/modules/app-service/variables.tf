variable "app_name" {
  description = "Name of the application"
  type        = string
}

variable "environment" {
  description = "Environment name (e.g. dev, prod)"
  type        = string
}

variable "location" {
  description = "The Azure region to deploy resources to"
  type        = string
}

variable "resource_group_name" {
  description = "Name of the resource group"
  type        = string
}

variable "subnet_id" {
  description = "ID of the subnet to integrate with App Service"
  type        = string
  default     = null
}

variable "sku_name" {
  description = "SKU name for the App Service Plan"
  type        = string
  default     = "B1" # Basic tier 1 - affordable for dev/test
}

variable "always_on" {
  description = "Keep the app loaded even when there's no traffic"
  type        = bool
  default     = true
}

variable "app_settings" {
  description = "Additional application settings for the App Service"
  type        = map(string)
  default     = {}
}

variable "tags" {
  description = "Tags to apply to all resources"
  type        = map(string)
  default     = {}
}