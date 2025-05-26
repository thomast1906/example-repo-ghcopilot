#!/bin/bash
# Script to create Azure Storage Account for Terraform state management

# Variables
RESOURCE_GROUP_NAME="terraform-state-rg"
STORAGE_ACCOUNT_NAME="tfstate$RANDOM"
CONTAINER_NAME="tfstate"
LOCATION="uksouth"

# Create resource group
echo "Creating resource group $RESOURCE_GROUP_NAME..."
az group create --name $RESOURCE_GROUP_NAME --location $LOCATION

# Create storage account
echo "Creating storage account $STORAGE_ACCOUNT_NAME..."
az storage account create \
    --resource-group $RESOURCE_GROUP_NAME \
    --name $STORAGE_ACCOUNT_NAME \
    --sku Standard_LRS \
    --encryption-services blob \
    --min-tls-version TLS1_2 \
    --allow-blob-public-access false

# Create storage container
echo "Creating storage container $CONTAINER_NAME..."
az storage container create \
    --name $CONTAINER_NAME \
    --account-name $STORAGE_ACCOUNT_NAME \
    --auth-mode login

# Get storage account key
STORAGE_ACCOUNT_KEY=$(az storage account keys list \
    --resource-group $RESOURCE_GROUP_NAME \
    --account-name $STORAGE_ACCOUNT_NAME \
    --query '[0].value' -o tsv)

# Output important information
echo "Resource Group: $RESOURCE_GROUP_NAME"
echo "Storage Account: $STORAGE_ACCOUNT_NAME"
echo "Container: $CONTAINER_NAME"

echo ""
echo "Configure your backend with:"
echo "----------------"
echo "terraform {"
echo "  backend \"azurerm\" {"
echo "    resource_group_name  = \"$RESOURCE_GROUP_NAME\""
echo "    storage_account_name = \"$STORAGE_ACCOUNT_NAME\""
echo "    container_name       = \"$CONTAINER_NAME\""
echo "    key                  = \"your-terraform-state-file-name.tfstate\""
echo "  }"
echo "}"
echo "----------------"

# Provide environment setup instructions
echo ""
echo "For GitHub Actions setup, add these secrets:"
echo "TERRAFORM_STORAGE_RG=$RESOURCE_GROUP_NAME"
echo "TERRAFORM_STORAGE_ACCOUNT=$STORAGE_ACCOUNT_NAME"
echo "TERRAFORM_CONTAINER=$CONTAINER_NAME"