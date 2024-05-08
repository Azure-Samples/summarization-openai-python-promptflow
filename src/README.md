# Hello world prompting with Azure Open AI

## Step 1: Set up your Azure AI project

### Step 1a: Use a cloud development environment

#### Explore sample with Codespaces

- To get started quickly with this sample, you can use a pre-built Codespaces development environment. **Click the button below** to open this repo in GitHub Codespaces, and then continue the readme!
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces)

- Once you've launched Codespaces you can proceed to step 2.

#### Start developing in an Azure AI curated VS Code development environment

- If you intend to develop your own code following this sample, we recommend you use the **Azure AI curated VS Code development environment**. It comes preconfigured with the Azure AI SDK packages that you will use to run this sample.
- You can get started with this cloud environment from the Azure AI Studio by following these steps: [Work with Azure AI projects in VS Code](https://learn.microsoft.com/azure/ai-studio/how-to/develop-in-vscode)

:grey_exclamation: **Important: If you are viewing this README from within this cloud VS Code environment, you can proceed directly to step 2!** This case will apply to you if you launched VS Code from an Azure AI Studio project. The Azure AI SDK packages including prompt flow are already installed.

### Step 1b: Alternatively, set up your local development environment

1. First, fork the repo, and then clone the code sample locally:

``` bash
git clone https://github.com/Azure-Samples/rag-data-openai-python-promptflow.git
cd src
```

1. Next, create a new Python virtual environment where we can safely install the SDK packages:

 * On MacOS and Linux run:

   ``` bash
   python3 --version
   python3 -m venv .venv
   ```

   ``` bash
   source .venv/bin/activate
   ```

* On Windows run:

   ``` bash
   py -3 --version
   py -3 -m venv .venv
   ```

   ``` bash
   .venv\scripts\activate
   ```

1. Now that your environment is activated, install the SDK packages

``` bash
pip install -r summarizationapp/requirements.txt
```

### Step 1c: Use the provision script to provision or reference Azure AI resources

The *provision.py* script will help provision the resources you need to run this sample. You specify your desired resources in the provision.yaml - there are notes in that file to help you. The script will check whether the resources you specified exist, otherwise it will create them. It will then construct a .env for you that references the provisioned or attached resources, including your keys. Once the provisioning is complete, you'll be ready to move to step 2.

:grey_exclamation: **Important: If you are viewing this README from within the cloud VS Code environment, the provisioning script will already have your subscription, hub and project details, and will extract other existing resources to set up your environment.**

``` bash
python provision.py --config provision.yaml --export-env .env --provision
```

## Step 2: Explore prompts

This sample repository contains a chat prompty file you can explore. This will let you verify your environment is set up to call your model deployment.

You can test your connection to your Azure Open AI model by running running your flow locally. Try changing up the specified system prompt to see how the model behaves with additional prompting.

``` bash
pf flow test --flow ./summarizationapp --inputs question="why is the sky blue?"
```

## Step 3: Test locally

Prompt flow provides an integrated front end to test chat applications. You can run with the `ui` flag to locally serve a web front end for testing. This will help you validate your inputs and outputs and test your chat functionality.

``` bash
pf flow test --flow ./summarizationapp --inputs question="why is the sky blue?" --ui
```

## Step 4: Deploy application to AI Studio

Use the deployment script to deploy your application to Azure AI Studio. This will deploy your app to a managed endpoint in Azure, that you can test, integrate into a front end application, or share with others.

``` bash
python deploy.py --deployment-name <deployment_name>
```

## Step 5: Verify your deployment

We recommend you follow the deployment link from the previous step to the test your application in the Azure AI Studio. If you prefer to test your endpoint locally, you can invoke it.

``` bash
python invoke.py --deployment-name <deployment_name>
```

Add the `--stream` argument if you want the response to be streamed.
