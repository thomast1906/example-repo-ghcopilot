# App Service Plan
resource "azurerm_service_plan" "app_service_plan" {
  name                = "${var.app_name}-${var.environment}-plan"
  location            = var.location
  resource_group_name = var.resource_group_name
  os_type             = "Linux"
  sku_name            = var.sku_name
  tags                = var.tags
}

# App Service for Flask Application
resource "azurerm_linux_web_app" "app_service" {
  name                = "${var.app_name}-${var.environment}-app"
  location            = var.location
  resource_group_name = var.resource_group_name
  service_plan_id     = azurerm_service_plan.app_service_plan.id
  
  https_only          = true  # Enforce HTTPS for security
  
  site_config {
    always_on        = var.always_on
    application_stack {
      python_version = "3.10"  # Match our python version
    }
    
    # Configuring health check for the app
    health_check_path = "/"
    
    # Basic IP restrictions for added security
    ip_restriction {
      action     = "Allow"
      priority   = 100
      name       = "AllowAll"  # In prod, you'd restrict to specific IPs
      ip_address = "0.0.0.0/0" # In prod, you'd use specific IP ranges
    }
  }
  
  # Environment variables - merge default and custom settings
  app_settings = merge({
    "WEBSITE_RUN_FROM_PACKAGE" = "1"
    "SCM_DO_BUILD_DURING_DEPLOYMENT" = "true"
    "PORT" = "8000"  # App Service expects apps to run on port 8000
  }, var.app_settings)
  
  # If provided, integrate with subnet
  dynamic "virtual_network_subnet_id" {
    for_each = var.subnet_id != null ? [var.subnet_id] : []
    content {
      subnet_id = var.subnet_id
    }
  }
  
  # Enable application logs for monitoring
  logs {
    application_logs {
      file_system_level = "Information"  # Log level
    }
    
    http_logs {
      file_system {
        retention_in_days = 7
        retention_in_mb   = 35
      }
    }
  }
  
  tags = var.tags
}