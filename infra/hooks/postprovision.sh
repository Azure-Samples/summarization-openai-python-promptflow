#!/bin/bash

echo  "Building summarizationapp:latest..."
az acr build --subscription ${AZURE_SUBSCRIPTION_ID} --registry ${AZURE_CONTAINER_REGISTRY_NAME} --image summarizationapp:latest ./src/
image_name="${AZURE_CONTAINER_REGISTRY_NAME}.azurecr.io/summarizationapp:latest"
az containerapp update --subscription ${AZURE_SUBSCRIPTION_ID} --name ${SERVICE_ACA_NAME} --resource-group ${RESOURCE_GROUP_NAME} --image ${image_name}
az containerapp ingress update --subscription ${AZURE_SUBSCRIPTION_ID} --name ${SERVICE_ACA_NAME} --resource-group ${RESOURCE_GROUP_NAME} --target-port 8080


echo "Starting postprovisioning..."
# Retrieve service names, resource group name, and other values from environment variables
resourceGroupName=$AZURE_RESOURCE_GROUP
echo resourceGroupName: $AZURE_RESOURCE_GROUP

openAiService=$AZURE_OPENAI_NAME
echo openAiService: $openAiService

subscriptionId=$AZURE_SUBSCRIPTION_ID
echo subscriptionId: $subscriptionId


# Ensure all required environment variables are set
if [ -z "$resourceGroupName" ] || [ -z "$openAiService" ] || [ -z "$subscriptionId" ]; then
    echo "One or more required environment variables are not set."
    echo "Ensure that AZURE_RESOURCE_GROUP, AZURE_OPENAI_NAME, AZURE_SUBSCRIPTION are set."
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
