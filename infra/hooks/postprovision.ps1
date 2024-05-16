#!/usr/bin/env pwsh

Write-Output  "Building summarizationapp:latest..."
az acr build --subscription $env:AZURE_SUBSCRIPTION_ID --registry $env:AZURE_CONTAINER_REGISTRY_NAME --image summarizationapp:latest ./src/
$image_name = $env:AZURE_CONTAINER_REGISTRY_NAME + '.azurecr.io/summarizationapp:latest'
az containerapp update --subscription $env:AZURE_SUBSCRIPTION_ID --name $env:SERVICE_ACA_NAME --resource-group $env:AZURE_OPENAI_RESOURCE_GROUP --image $image_name
az containerapp ingress update --subspription $env:AZURE_SUBSCRIPTION_ID --name $env:SERVICE_ACA_NAME --resource-group $env:AZURE_OPENAI_RESOURCE_GROUP --target-port 8080

# Retrieve service names, resource group name, and other values from environment variables
$resourceGroupName = $env:AZURE_RESOURCE_GROUP
Write-Host "resourceGroupName: $resourceGroupName"

$openAiService = $env:AZURE_OPENAI_NAME
Write-Host "openAiService: $openAiService"

$subscriptionId = $env:AZURE_SUBSCRIPTION_ID
Write-Host "subscriptionId: $subscriptionId"


# Ensure all required environment variables are set
if ([string]::IsNullOrEmpty($resourceGroupName) -or [string]::IsNullOrEmpty($openAiService) -or [string]::IsNullOrEmpty($subscriptionId)) {
    Write-Host "One or more required environment variables are not set."
    Write-Host "Ensure that AZURE_RESOURCE_GROUP, AZURE_OPENAI_NAME, AZURE_SUBSCRIPTION_ID are set."
    exit 1
}

# Retrieve the keys
$apiKey = (az cognitiveservices account keys list --name $openAiService --resource-group $resourceGroupName --query key1 --output tsv)

# Set the environment variables using azd env set
azd env set AZURE_OPENAI_API_VERSION 2023-03-15-preview
azd env set AZURE_OPENAI_CHAT_DEPLOYMENT gpt-35-turbo

# Output environment variables to .env file using azd env get-values
azd env get-values > ./src/summarizationapp/.env