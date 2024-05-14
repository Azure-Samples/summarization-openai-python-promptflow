#!/bin/sh

echo "Starting postprovisioning..."
# Retrieve service names, resource group name, and other values from environment variables
resourceGroupName=$AZURE_RESOURCE_GROUP
echo resourceGroupName: $AZURE_RESOURCE_GROUP

openAiService=$AZURE_OPENAI_NAME
echo openAiService: $openAiService

subscriptionId=$AZURE_SUBSCRIPTION_ID
echo subscriptionId: $subscriptionId

aiProjectName=$AZUREAI_PROJECT_NAME
echo aiProjectName: $aiProjectName


# Ensure all required environment variables are set
if [ -z "$resourceGroupName" ] || [ -z "$openAiService" ] || [ -z "$subscriptionId" ] || [ -z "$aiProjectName" ]; then
    echo "One or more required environment variables are not set."
    echo "Ensure that AZURE_RESOURCE_GROUP, AZURE_OPENAI_NAME, AZURE_SUBSCRIPTION_ID, and AZUREAI_PROJECT_NAME are set."
    exit 1
fi

# Retrieve the keys
apiKey=$(az cognitiveservices  account keys list --name $openAiService --resource-group $resourceGroupName --subscription $subscriptionId --query key1 --output tsv)

# Set the environment variables using azd env set
azd env set AZURE_OPENAI_API_KEY $apiKey
azd env set AZURE_OPENAI_KEY $apiKey
azd env set AZURE_OPENAI_API_VERSION 2023-03-15-preview
azd env set AZURE_OPENAI_CHAT_DEPLOYMENT gpt-35-turbo

# Output environment variables to .env file using azd env get-values
azd env get-values > ./src/summarizationapp/.env

echo "Script execution completed successfully."

echo 'Installing dependencies from "requirements.txt"'
python3 -m pip install -r ./src/summarizationapp/requirements.txt
