output "vnet_id" {
  description = "ID of the created virtual network"
  value       = azurerm_virtual_network.vnet.id
}

output "subnet_id" {
  description = "ID of the created subnet"
  value       = azurerm_subnet.app_subnet.id
}

output "subnet_name" {
  description = "Name of the created subnet"
  value       = azurerm_subnet.app_subnet.name
}