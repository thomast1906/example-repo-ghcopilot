module "flask_app" {
  source = "../../"
  
  # Production environment specific variables
  environment         = "prod"
  resource_group_name = "flask-app-prod-rg"
  app_name            = "flask-web-app"
  location            = "uksouth" # As required: UK South
  
  # For production, use a more robust SKU
  sku_name            = "P1v2" # Premium v2 small instance
  always_on           = true   # Always keep the app running
  
  tags = {
    Application = "Flask Web App"
    Environment = "Production"
    ManagedBy   = "Terraform"
    CostCenter  = "Operations"
    Criticality = "High"
  }
}