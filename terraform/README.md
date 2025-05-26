# Terraform for Flask Application on Azure

This directory contains Terraform infrastructure as code (IaC) for deploying the Flask application to Azure App Service.

## Architecture

The Terraform configuration creates the following resources:
- Resource Group to logically contain all resources
- Virtual Network and Subnet for network isolation
- App Service Plan to define the compute resources
- App Service to host the Flask application
- Application Insights for monitoring and diagnostics

## Directory Structure

```
terraform/
├── modules/                  # Reusable Terraform modules
│   ├── app-service/          # App Service module
│   └── network/              # Network module
├── environments/             # Environment-specific configurations
│   ├── dev/                  # Development environment
│   └── prod/                 # Production environment
├── backend.tf                # Terraform state backend configuration
├── main.tf                   # Main Terraform configuration
├── variables.tf              # Input variables definition
└── outputs.tf                # Output values
```

## Usage

### Prerequisites

- Azure subscription
- Terraform CLI (version 1.0.0 or newer)
- Azure CLI
- Storage account for Terraform state (see backend.tf)

### Deploying to Development

```bash
cd terraform/environments/dev
terraform init -backend-config=../../../backend-config/dev.tfvars
terraform plan
terraform apply
```

### Deploying to Production

```bash
cd terraform/environments/prod
terraform init -backend-config=../../../backend-config/prod.tfvars
terraform plan
terraform apply
```

## Security Features

- HTTPS enforcement
- Network isolation capabilities with Virtual Network integration
- Application Insights for monitoring and security analysis
- Health checks for application availability

## Compliance

This Terraform configuration is designed to align with:
- Azure Well-Architected Framework
- Terraform best practices
- Security best practices for web applications

## GitHub Actions Integration

The GitHub Actions workflow in `.github/workflows/deploy-terraform.yaml` automates the deployment of this infrastructure. See the workflow file for more details.