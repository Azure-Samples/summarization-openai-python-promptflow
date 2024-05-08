Write-Host "Starting postprovisioning..."

# Retrieve service names, resource group name, and other values from environment variables
$resourceGroupName = $env:AZURE_RESOURCE_GROUP
Write-Host "resourceGroupName: $resourceGroupName"

$openAiService = $env:AZURE_OPENAI_NAME
Write-Host "openAiService: $openAiService"

$subscriptionId = $env:AZURE_SUBSCRIPTION_ID
Write-Host "subscriptionId: $subscriptionId"

$aiProjectName = $env:AZUREAI_PROJECT_NAME
Write-Host "aiProjectName: $aiProjectName"

# Ensure all required environment variables are set
if ([string]::IsNullOrEmpty($resourceGroupName) -or [string]::IsNullOrEmpty($openAiService) -or [string]::IsNullOrEmpty($subscriptionId) -or [string]::IsNullOrEmpty($aiProjectName)) {
    Write-Host "One or more required environment variables are not set."
    Write-Host "Ensure that AZURE_RESOURCE_GROUP, AZURE_OPENAI_NAME, AZURE_SUBSCRIPTION_ID, and AZUREAI_PROJECT_NAME are set."
    exit 1
}

# Retrieve the keys
$apiKey = (az cognitiveservices account keys list --name $openAiService --resource-group $resourceGroupName --query key1 --output tsv)

# Set the environment variables using azd env set
azd env set AZURE_OPENAI_API_KEY $apiKey
azd env set AZURE_OPENAI_KEY $apiKey
azd env set AZURE_OPENAI_API_VERSION 2023-03-15-preview
azd env set AZURE_OPENAI_CHAT_DEPLOYMENT gpt-35-turbo

# Output environment variables to .env file using azd env get-values
azd env get-values > ./src/summarizationapp/.env

Write-Host "Script execution completed successfully."

Write-Host 'Installing dependencies from "requirements.txt"'
python -m pip install -r src/summarizationapp/requirements.txt