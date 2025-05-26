output "app_service_url" {
  description = "The URL of the App Service"
  value       = module.app_service.app_service_url
}

output "resource_group_name" {
  description = "The name of the resource group"
  value       = azurerm_resource_group.rg.name
}

output "app_insights_instrumentation_key" {
  description = "The Application Insights instrumentation key"
  value       = azurerm_application_insights.app_insights.instrumentation_key
  sensitive   = true # Marked as sensitive to prevent showing in logs
}

output "vnet_id" {
  description = "The ID of the Virtual Network"
  value       = module.network.vnet_id
}

output "app_service_name" {
  description = "The name of the App Service"
  value       = module.app_service.app_service_name
}