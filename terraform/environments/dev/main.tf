module "flask_app" {
  source = "../../"
  
  # Dev environment specific variables
  environment         = "dev"
  resource_group_name = "flask-app-dev-rg"
  app_name            = "flask-web-app"
  location            = "uksouth" # As required: UK South
  
  tags = {
    Application = "Flask Web App"
    Environment = "Development"
    ManagedBy   = "Terraform"
    CostCenter  = "DevOps"
  }
}