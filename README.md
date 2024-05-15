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

Samples in JavaScript, Python, and Java. Learn more at [https://aka.ms/azai](https://aka.ms/azai).
---

## Table of Contents

- [Features](#features)
- [Architecture Diagram](#architecture-diagram)
- [Azure Deployment](#azure-deployment)
  - [Cost estimation](#cost-estimation)
  - [Project setup](#project-setup)
    - [GitHub Codespaces](#github-codespaces)
    - [VS Code Dev Containers](#vs-code-dev-containers)
    - [Local environment](#local-environment)
- [Deploying](#deploying)
- [Using the app](#using-the-app)
  - [Explore the prompty file](#explore-the-prompty-file)
  - [Testing the sample](#testing-the-sample)
- [Contributing](#contributing)
- [Code of Conduct](code-of-conduct)


[![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=GitHub+Codespaces&message=Open&color=brightgreen&logo=github)](https://github.com/codespaces/new?hide_repo_select=true&ref=main&repo=599293758&machine=standardLinux32gb&devcontainer_path=.devcontainer%2Fdevcontainer.json&location=WestUs2)
[![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/Azure-Samples/chat-rag-openai-csharp-prompty) 

In this sample we recieve issues reported by field and shop floor workers at a company called Contoso Manufacturing, a manufacturing company that makes car batteries. The issues are shared by the workers either live through microphone input, pre-recorded as audio files or as text input. We translate audio input from speech to text and then use the text reports as input to an LLM and Prompty/Promptflow to summarize the issue and return the results in a format we specify.

This sample uses the **[Azure AI Speech Service](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/)** and **[Python SDk](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/quickstarts/setup-platform?pivots=programming-language-python&tabs=macos%2Cubuntu%2Cdotnetcli%2Cdotnet%2Cjre%2Cmaven%2Cnodejs%2Cmac%2Cvscode)** to translate the users speech into text. It leverages **[Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/)** to summarize the text and **[Prompty and Prompt Flow](https://microsoft.github.io/promptflow/how-to-guides/develop-a-prompty/index.html)** to create, manage and evaluate the prompt into our code.

## Features

This project template provides the following features:

* `speech_to_text.py` file that converts microphone input or pre-recorded audio to text.
* Pre-recorded audio files in the `ticket-processing/data/` folder to use for testing the app.
* `summarize.prompty` file where the prompt is constructed and edited.
* `requirements.txt` file with all the python packages needed to run this example.
* A bicep file to help provision and deploy your app using azd 
* You will be able to use this app with Azure AI Studio

## Architecture Diagram
![Architecture Digram](https://github.com/Azure-Samples/summarization-openai-python-promptflow/blob/main/images/architecture-diagram-summarization-aistudio.png)

### Azure account requirements

**IMPORTANT:** In order to deploy and run this example, you'll need:

* **Azure account**. If you're new to Azure, [get an Azure account for free](https://azure.microsoft.com/free/cognitive-search/) and you'll get some free Azure credits to get started. See [guide to deploying with the free trial](docs/deploy_lowcost.md).
* **Azure subscription with access enabled for the Azure OpenAI service**. You can request access with [this form](https://aka.ms/oaiapply). If your access request to Azure OpenAI service doesn't match the [acceptance criteria](https://learn.microsoft.com/legal/cognitive-services/openai/limited-access?context=%2Fazure%2Fcognitive-services%2Fopenai%2Fcontext%2Fcontext), you can use [OpenAI public API](https://platform.openai.com/docs/api-reference/introduction) instead.
    - Ability to deploy `gpt-35-turbo`
    - We recommend using Sweden Central or East US 2
* **Azure subscription with access enabled for [Azure AI Speech Service](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/)**
* **Azure account permissions**:
  * Your Azure account must have `Microsoft.Authorization/roleAssignments/write` permissions, such as [Role Based Access Control Administrator](https://learn.microsoft.com/azure/role-based-access-control/built-in-roles#role-based-access-control-administrator-preview), [User Access Administrator](https://learn.microsoft.com/azure/role-based-access-control/built-in-roles#user-access-administrator), or [Owner](https://learn.microsoft.com/azure/role-based-access-control/built-in-roles#owner). If you don't have subscription-level permissions, you must be granted [RBAC](https://learn.microsoft.com/azure/role-based-access-control/built-in-roles#role-based-access-control-administrator-preview) for an existing resource group and [deploy to that existing group](docs/deploy_existing.md#resource-group).
  * Your Azure account also needs `Microsoft.Resources/deployments/write` permissions on the subscription level.

## Azure deployment

### Cost estimation

Pricing varies per region and usage, so it isn't possible to predict exact costs for your usage.
However, you can try the [Azure pricing calculator](https://azure.com/e/d18187516e9e421e925b3b311eec8aae) for the resources below.

- Azure OpenAI: Standard tier, GPT and Ada models. Pricing per 1K tokens used, and at least 1K tokens are used per question. [Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/)
- Azure AI Speech: Free tier, this provides you with 5 audio hours free per month. [Pricing](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/speech-services/) 

### Project setup

You have a few options for setting up this project.
The easiest way to get started is GitHub Codespaces, since it will setup all the tools for you.
Here are the three options in increasing order of complexity and effort on your part. 

Pick one!

 1. Pre-built environment, in cloud with GitHub Codespaces (recommended)
 2. Pre-built environment, on device with VS Code Dev Containers
 3. Manual setup environment, on device with Anaconda or venv

#### GitHub Codespaces

**This is the recommended option!**
You can run this repo virtually by using GitHub Codespaces, which will open a web-based VS Code in your browser. To run code spaces:
 - Fork the repo into your personal profile.
 - In your fork, click the green Code button on the repository
 - Select the `Codespaces` tab and click `Create codespace...`

   You can also click this button:
  [![Open in GitHub Codespaces](https://img.shields.io/static/v1?style=for-the-badge&label=GitHub+Codespaces&message=Open&color=brightgreen&logo=github)](https://codespaces.new/Azure-Samples/summarization-openai-python-promptflow)

Once the codespace opens (this may take several minutes), open a terminal window.

**Congratulations! Your cloud dev environment is ready!**

Once you've launched Codespaces you can proceed to [step 2](#step-2-create-azure-resources).

#### VS Code Dev Containers

A related option is VS Code Dev Containers, which will open the project in your local VS Code using the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):

1. Start Docker Desktop (install it if not already installed)
2. Open the project:
    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/Azure-Samples/summarization-openai-python-promptflow.git)
3. In the VS Code window that opens, once the project files show up (this may take several minutes), open a terminal window.

**Congratulations! Your local dev environment is ready!**

- Once you've launched your docker container environment you can proceed to [step 2](#step-2-create-azure-resource).

#### Local environment

1. Install the required tools:

    * [Azure Developer CLI](https://aka.ms/azure-dev/install)
    * [Python 3.9, 3.10, or 3.11](https://www.python.org/downloads/)
      * **Important**: Python and the pip package manager must be in the path in Windows for the setup scripts to work.
      * **Important**: Ensure you can run `python --version` from console. On Ubuntu, you might need to run `sudo apt install python-is-python3` to link `python` to `python3`.
    * [Node.js 14+](https://nodejs.org/en/download/)
    * [Git](https://git-scm.com/downloads)
    * [Powershell 7+ (pwsh)](https://github.com/powershell/powershell) - For Windows users only.
      * **Important**: Ensure you can run `pwsh.exe` from a PowerShell terminal. If this fails, you likely need to upgrade PowerShell.

2. Create a new folder and switch to it in the terminal.
3. Run this command to download the project code:

    ```shell
    azd init -t summarization-openai-python-promptflow
    ```

    Note that this command will initialize a git repository, so you do not need to clone this repository.

### Deploying

Follow these steps to provision Azure resources and deploy the application code:

1. Login to your Azure account:

    ```shell
    azd auth login
    ```

2. Create a new azd environment:

    ```shell
    azd env new
    ```

    Enter a name that will be used for the resource group.
    This will create a new folder in the `.azure` folder, and set it as the active environment for any     calls to `azd` going forward.

3. Run `azd up` - This will provision Azure resources and deploy this sample to those resources.
   You will be prompted to select two locations, one for the majority of resources and one for the OpenAI resource, which is currently a short list. That location list is based on the [OpenAI model availability table](https://learn.microsoft.com/azure/cognitive-services/openai/concepts/models#model-summary-table-and-region-availability) and may become outdated as availability changes. For this sample we recommend using either Sweden Central or US East 2.

## Using the app

### Explore the prompty file

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

### Testing the sample

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

## Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).

Resources:

- [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)
- [Microsoft Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
- Contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with questions or concerns


For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
