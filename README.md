---
name: Process Automation - Speech to Text and Summarization with AI Studio
description: Use Azure AI Studio for speech to text conversion and summarization with LLMs 
languages:
- python
- typescript
- bicep
- azdeveloper
products:
- azure-openai
- azure-cognitive-speech-sdk
- azure
page_type: sample
urlFragment: summarization-openai-python-promptflow
---

# Process Automation: Speech to Text and Summarization with AI Studio

In this sample we recieve issues reported by field and shop floor workers at a company called Contoso Manufacturing, a manufacturing company that makes car batteries. The issues are shared by the workers either live through microphone input, pre-recorded as audio files or as text input. We translate audio input from speech to text and then use the text reports as input to an LLM and Prompty/Promptflow to summarize the issue and return the results in a format we specify.

# Process Automation: Speech to Text and Summarization with AI Studio

This sample uses the **[Azure AI Speech Service](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/)** and **[Python SDk](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/quickstarts/setup-platform?pivots=programming-language-python&tabs=macos%2Cubuntu%2Cdotnetcli%2Cdotnet%2Cjre%2Cmaven%2Cnodejs%2Cmac%2Cvscode)** to translate the users speech into text. It leverages **[Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/)** to summarize the text and **[Prompty and Prompt Flow](https://microsoft.github.io/promptflow/how-to-guides/develop-a-prompty/index.html)** to create, manage and evaluate the prompt into our code.

By the end of deploying this template you should be able to:

 1. Describe what Azure AI Speech Service Python SDK provides.
 2. Explain prompt creation with Prompty and Prompt Flow. 
 3. Build, run, evaluate and deploy, the summarization app to Azure.

## Features

This project template provides the following features:

* `speech_to_text.py` file that converts microphone input or pre-recorded audio to text.
* Pre-recorded audio files in the `ticket-processing/data/` folder to use for testing the app.
* `summarize.prompty` file where the prompt is constructed and edited.
* `requirements.txt` file with all the python packages needed to run this example.
* A bicep file to help provision and deploy your app using azd 
* You will be able to use this app with Azure AI Studio

### Architecture Diagram
![Architecture Digram](https://github.com/Azure-Samples/summarization-openai-python-promptflow/blob/main/images/architecture-diagram-summarization-aistudio.png)

## Getting Started

### Prerequisites

- **Azure Subscription** - [Signup for a free account.](https://azure.microsoft.com/free/)
- **Visual Studio Code** - [Download it for free.](https://code.visualstudio.com/download)
- **GitHub Account** - [Signup for a free account.](https://github.com/signup)
- **Access to Azure Open AI Services** - [Learn about getting access.](https://learn.microsoft.com/legal/cognitive-services/openai/limited-access)

**IMPORTANT:** In order to deploy and run this example, you'll need:

* **Azure subscription with access enabled for the Azure OpenAI service**. You can request access with [this form](https://aka.ms/oaiapply).
    - Ability to deploy these models - `gpt-35-turbo`, `gpt-4`, `text-embeddings-ada-002`
    - We recommend using Sweden Central or East US 2
* **Azure account permissions**:
  * Your Azure account must have `Microsoft.Authorization/roleAssignments/write` permissions, such as [Role Based Access Control Administrator](https://learn.microsoft.com/azure/role-based-access-control/built-in-roles#role-based-access-control-administrator-preview), [User Access Administrator](https://learn.microsoft.com/azure/role-based-access-control/built-in-roles#user-access-administrator), or [Owner](https://learn.microsoft.com/azure/role-based-access-control/built-in-roles#owner). If you don't have subscription-level permissions, you must be granted [RBAC](https://learn.microsoft.com/azure/role-based-access-control/built-in-roles#role-based-access-control-administrator-preview) for an existing resource group and [deploy to that existing group](docs/deploy_existing.md#resource-group).
  * Your Azure account also needs `Microsoft.Resources/deployments/write` permissions on the subscription level.

### AZD
- **Install [azd](https://aka.ms/install-azd)**
    - Windows: `winget install microsoft.azd`
    - Linux: `curl -fsSL https://aka.ms/install-azd.sh | bash`
    - MacOS: `brew tap azure/azd && brew install azd`


## Step 1: Development Environment

The repository is instrumented with a `devcontainer.json` configuration that can provide you with a _pre-built_ environment that can be launched locally, or in the cloud. You can also elect to do a _manual_ environment setup locally, if desired. Here are the three options in increasing order of complexity and effort on your part. **Pick one!**

 1. **Pre-built environment, in cloud** with GitHub Codespaces
 2. **Pre-built environment, on device** with Docker Desktop
 3. **Manual setup environment, on device** with Anaconda or venv

The first approach is _recommended_ for minimal user effort in startup and maintenance. The third approach will require you to manually update or maintain your local environment, to reflect any future updates to the repo.

To setup the development environment you can leverage either GitHub Codespaces, a local Python environment (using Anaconda or venv), or a VS Code Dev Container environment (using Docker).

### Step 1.1: Pre-Built Environment, in cloud (GitHub Codespaces)

**This is the recommended option.**
 - Fork the repo into your personal profile.
 - In your fork, click the green `Code` button on the repository
 - Select the `Codespaces` tab and click `Create codespace...` You can also click this button:
[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Azure-Samples/summarization-openai-python-promptflow)

This should open a new browser tab with a Codespaces container setup process running. On completion, this will launch a Visual Studio Code editor in the browser, with all relevant dependencies already installed in the running development container beneath. **Congratulations! Your cloud dev environment is ready!**

- Once you've launched Codespaces you can proceed to [step 2](#step-2-create-azure-resources).

### Step 1.2: Pre-Built Environment, on device (Docker Desktop)

This option uses the same `devcontainer.json` configuration, but launches the development container in your local device using Docker Desktop. To use this approach, you need to have the following tools pre-installed in your local device:
 - Visual Studio Code (with Dev Containers Extension)
 - Docker Desktop (community or free version is fine)

**Make sure your Docker Desktop daemon is running on your local device.** Then,
 - Fork this repo to your personal profile
 - Clone that fork to your local device
 - Open the cloned repo using Visual Studio Code

If your Dev Containers extension is installed correctly, you will be prompted to "re-open the project in a container" - just confirm to launch the container locally. Alternatively, you may need to trigger this step manually. See the [Dev Containers Extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers) for more information.

Once your project launches in the local Docker desktop container, you should see the Visual Studio Code editor reflect that connection in the status bar (blue icon, bottom left). **Congratulations! Your local dev environment is ready!**

- Once you've launched your docker container environment you can proceed to [step 2]().

### Step 1.3: Manual Setup Environment, on device (Anaconda or venv)

#### Local Requirements
In order to run this sample locally you will need to: 

If all of the above are correctly installed you can set up your local developer environment as follows. 

1. First, fork the repo, and then clone the code sample locally: 

   ``` bash
   git clone https://github.com/Azure-Samples/summarization-openai-python-promptflow.git
   ```

2. Open the repo in VS Code and navgate to the src directory

   ```bash
   cd summarization-openai-python-promptflow
   code .
   cd src/summarizationapp
   ```

3. Install the [Prompt Flow Extension](https://marketplace.visualstudio.com/items?itemName=prompt-flow.prompt-flow) in VS Code
      - Open the VS Code Extensions tab
      - Search for "Prompt Flow"
      - Install the extension

4. Install the [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) for your device OS

5. Create a new local Python environment using **either** [anaconda](https://www.anaconda.com/products/individual) **or** [venv](https://docs.python.org/3/library/venv.html) for a managed environment.

    a. **Option 1**: Using anaconda

        ```
        conda create -n summarization-promptflow python=3.11
        conda activate summarization-promptflow
        pip install -r requirements.txt
        ```

    b. **Option 2:** Using venv

        ```
        python3 -m venv .venv
        source .venv/bin/activate
        pip install -r requirements.txt
        
## Step 2: Install `azd` and deploy with `azd up`
- If you setup your development environment manually, follow [these instructions](https://learn.microsoft.com/azure/developer/azure-developer-cli/install-azd?tabs=winget-windows%2Cbrew-mac%2Cscript-linux&pivots=os-windows) to install `azd` for your local device OS.
- If you used a pre-built dev container environment (e.g., GitHub Codespaces or Docker Desktop) the tool is pre-installed for you.
- Verify that the tool is installed by typing ```azd version``` in a terminal.

#### Authenticate with Azure
- Start the authentication flow from a terminal:
    ```bash
    azd auth login
    ```
- This should activate a Device Code authentication flow as shown below. Just follow the instructions and complete the auth flow till you get the `Logged in on Azure` message indicating success.
    ```bash
    Start by copying the next code: <code-here>
    Then press enter and continue to log in from your browser...
    ```

- Run this unified command to provision all resources. This will take a non-trivial amount of time to complete.
    ```bash
    azd up
    ```
- You will be prompted for the subscription you want you use and the region. The bicep parameters declare two location fields: the first one is the primary location for all resources, the second is a location field specifically for where the OpenAI resource should be created.

- On completion, it automatically invokes a`postprovision.sh` script that will attempt to log you into Azure. You may see something like this. Just follow the provided instructions to complete the authentication flow.
    ```bash
    No Azure user signed in. Please login.
    ```
- Once logged in, the script will do the following for you:
    - Download `config.json` to the local device
    - Populate `.env` with required environment variables
    - Populate your data (in Azure AI Search, Azure CosmosDB)
    - Create relevant Connections (for prompt flow)
    - Upload your prompt flow to Azure (for deployment)

That's it! You should now be ready to continue the process as before. Note that this is a new process so there may be some issues to iron out. Start by completing the verification steps below and taking any troubleshooting actions identified.

#### Verify Provisioning

The script should **set up a dedicated resource group** with the following resources:

 - **Azure AI services** resource
 - **Azure Container app** resource
 - **Azure Open AI Service** resource
 - **Azure Speech to Text** resource

#### Verify `.env` setup

The default sample has an `.env.sample` file in the `summarizationapp` folder that shows the relevant environment variables that need to be configured in this project. The script should create a `.env` file that has these same variables _but populated with the right values_ for your Azure resources.

If the file is not created, copy over `.env.sample` to `.env` - then populate those values manually from the respective Azure resource pages using the Azure AI Studio (for the Azure OpenAI values). 

## Step 3: Explore the `summarize.prompty` file

This sample repository contains a summarize prompty file you can explore. In this sample we are telling the model to summarize the reports given by a worker in a specific format. 

The prompty file contains the following:
- The `name`, `description` and `authors` of the prompt
- `configuration`: Details about the LLM model including:
  - api type: chat or completion
  - configuration: connection type (azure_openai or openai) and environment variables
  - model parametes: max_tokesn, temperature and response_format (text or json_object)
- `inputs`: the content input from the user, where each input should have a type and can also have a default value
- `outputs`: where the output should have a type like string
- Sample Section: a sample of the inputs to be provided
- The prompt: in this sample we send add a `system message` as the prompt with context and details about the format. We also add in a `user message` at the bottom of the file, which consists of the reported issue in text format from our user. 

If you ran the provisioning step above correctly, all of the variables should already be set for you. You can edit the prompt to see what changes this makes to the summary created. 

## Step 4: Testing the sample

This repository contains sample data to be able to test the project end to end. To run this project you'll need to pass in as input a reported issue to be summarized. You can pass this input as either a `.wav` file or a string of text. The `data/audio-data/` folder contains sample audio files for you to use or you can use the example string shown below. Below are the commands you can use in your terminal to run the project locally with promptflow.

Testing with sample audio data: 
``` bash
pf flow test --flow ./src/summarizationapp --inputs problem="data/audio-data/issue0.wav"
```

Testing with sample text data:
``` bash
pf flow test --flow ./src/summarizationapp --inputs problem="I need to open a problem report for part number ABC123. The brake rotor is overheating causing glazing on the pads. We track temperature above 24 degrees Celsius and we are seeing this after three to four laps during runs when the driver is braking late and aggressively into corners. The issue severity is to be prioritized as a 2. This is impacting the front brake assembly EFG234"
```

To understand how the code works look through the `speech_to_text.py` file. 

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

## Microsoft Open Source Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).

Resources:

- [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)
- [Microsoft Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
- Contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with questions or concerns


For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
