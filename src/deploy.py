from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
from azure.ai.ml.entities import ManagedOnlineEndpoint, ManagedOnlineDeployment, Model, Environment, BuildContext

import os
from dotenv import load_dotenv
load_dotenv()

def deploy_flow(deployment_name):

    client = MLClient.from_config(DefaultAzureCredential())

    endpoint_name = f"{deployment_name}-endpoint"

    endpoint = ManagedOnlineEndpoint(
        name=endpoint_name,
        properties={
            "enforce_access_to_default_secret_stores": "enabled" # if you want secret injection support
        }
    )

    deployment = ManagedOnlineDeployment( # defaults to key auth_mode
        name=deployment_name,
        endpoint_name=endpoint_name,
        model=Model(path="./summarizationapp"), # path to prompt flow folder
        environment=Environment( # when pf is a model type, the environment section will not be required at all
            build=BuildContext(
                path="./summarizationapp",
            ),
            inference_config={
                "liveness_route": {
                    "path": "/health",
                    "port": 8080,
                },
                "readiness_route": {
                    "path": "/health",
                    "port": 8080,
                },
                "scoring_route":{
                    "path": "/score",
                    "port": 8080,
                },
            },
        ),
        instance_type="Standard_E16s_v3", # can point to documentation for this: https://learn.microsoft.com/en-us/azure/machine-learning/reference-managed-online-endpoints-vm-sku-list?view=azureml-api-2
        instance_count=1,
        environment_variables={  # when pf is a model type, this section will not be required at all
            "PRT_CONFIG_OVERRIDE": f"deployment.subscription_id={client.subscription_id},deployment.resource_group={client.resource_group_name},deployment.workspace_name={client.workspace_name},deployment.endpoint_name={endpoint_name},deployment.deployment_name={deployment_name}",
            'AZURE_OPENAI_ENDPOINT': "${{azureml://connections/Default_AzureOpenAI/target}}",
            'OPENAI_API_KEY': "${{azureml://connections/Default_AzureOpenAI/credentials/key}}",
            'AZURE_OPENAI_KEY': "${{azureml://connections/Default_AzureOpenAI/credentials/key}}",
            'AZURE_OPENAI_API_VERSION': "${{azureml://connections/Default_AzureOpenAI/metadata/ApiVersion}}",
            'AZURE_AI_SEARCH_ENDPOINT': "${{azureml://connections/AzureAISearch/target}}",
            'AZURE_AI_SEARCH_KEY': "${{azureml://connections/AzureAISearch/credentials/key}}",
            'AZURE_AI_SEARCH_INDEX_NAME': os.getenv('AZURE_AI_SEARCH_INDEX_NAME'),
            'AZURE_OPENAI_CHAT_MODEL': os.getenv('AZURE_OPENAI_CHAT_MODEL'),
            'AZURE_OPENAI_CHAT_DEPLOYMENT': os.getenv('AZURE_OPENAI_CHAT_DEPLOYMENT'),
            'AZURE_OPENAI_EVALUATION_MODEL': os.getenv('AZURE_OPENAI_EVALUATION_MODEL'),
            'AZURE_OPENAI_EVALUATION_DEPLOYMENT': os.getenv('AZURE_OPENAI_EVALUATION_DEPLOYMENT'),
            'AZURE_OPENAI_EMBEDDING_MODEL': os.getenv('AZURE_OPENAI_EMBEDDING_MODEL'),
            'AZURE_OPENAI_EMBEDDING_DEPLOYMENT': os.getenv('AZURE_OPENAI_EMBEDDING_DEPLOYMENT'),
        }
    )

    # 1. create endpoint
    created_endpoint = client.begin_create_or_update(endpoint).result() # result() means we wait on this to complete - currently endpoint doesnt have any status, but then deployment does have status

    # 2. create deployment
    created_deployment = client.begin_create_or_update(deployment).result()

    # 3. update endpoint traffic for the deployment
    endpoint.traffic = {deployment_name: 100} # 100% of traffic
    client.begin_create_or_update(endpoint).result()

    return created_endpoint, created_deployment

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--deployment-name", help="deployment name used to deploy to a managed online endpoint in AI Studio", type=str)
    args = parser.parse_args()

    deployment_name = args.deployment_name if args.deployment_name else f"sdk-copilot"

    deploy_flow(deployment_name)