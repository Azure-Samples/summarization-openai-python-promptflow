from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

def invoke_deployment(client: MLClient, deployment_name: str, stream: bool = False):
    import requests

    if stream:
        accept_header = "application/jsonl"
    else:
        accept_header = "application/json"

    scoring_url = client.deployments.get(deployment_name).scoring_uri
    primary_key = client.deployments.get_keys(deployment_name).primary_key

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {primary_key}",
        "Accept": accept_header,
        "azureml-model-deployment": deployment_name,
    }

    response = requests.post(
        scoring_url,
        headers=headers,
        json={
            "messages": [{"role": "user", "content": "How much do the Trailwalker shoes cost?"}],
            "stream": stream,
        },
        stream=stream
    )
    if stream:
        for item in response.iter_lines(chunk_size=None):
            print(item)
    else:
        fullResponse = response.json()
        assistantResponse = fullResponse['choices'][0]['message']['content'] # needs clean up
        print(assistantResponse)
        print("\n")
        print(fullResponse["usage"])


if __name__ == "__main__":
  # Parse command line arguments
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument("--deployment-name", help="deployment name to use when deploying or invoking the flow", type=str)
  parser.add_argument("--stream", help="Whether response from a particular implementation should be streamed or not", action="store_true")
  args = parser.parse_args()
  deployment_name = args.deployment_name if args.deployment_name else None

  client = MLClient.from_config(DefaultAzureCredential()) # need not from config here

  if not deployment_name:
      deployment_name = f"{client.project_name}-copilot"
  invoke_deployment(client, deployment_name, stream=args.stream)