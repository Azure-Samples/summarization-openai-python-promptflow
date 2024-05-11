---
name: Ticket Processing with Azure AI
description: Process tickets automatically with .
languages:
- python
- typescript
- bicep
- azdeveloper
products:
- azure-openai
- azure-cognitive-search
- azure
page_type: sample
urlFragment: azure-search-openai-demo
---

# Ticket Processing using Azure AI

In this sample we recieve issues reported by field and shop floor workers at a company called Contoso Manufacturing, a manufacturing company that makes car batteries. The issues are shared by the workers either live through microphone input or pre-recorded as audio files. We translate the input from speech to text and then use an LLM and Prompty/Promptflow to summarize the issue and return the results in a format we specify.

# Ticket Processing using Azure AI 

This sample uses the **[Azure AI Speech Service](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/)** and **[Python SDk](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/quickstarts/setup-platform?pivots=programming-language-python&tabs=macos%2Cubuntu%2Cdotnetcli%2Cdotnet%2Cjre%2Cmaven%2Cnodejs%2Cmac%2Cvscode)** to translate the users speech into text. It leverages **[Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/)** to summarize the text and **[Prompty and Prompt Flow](https://microsoft.github.io/promptflow/how-to-guides/develop-a-prompty/index.html)** to create, manage and evaluate the prompt into our code.

By the end of deploying this template you should be able to:

 1. Describe what Azure AI Speech Service Python SDK provides.
 2. Explain prompt creation with Prompty and Prompt Flow. 
 3. Build, run, evaluate and deploy, the summarization app to Azure.

## Features

This project template provides the following features:

* A `speech_to_text.py` file that converts microphone input or pre-recorded audio to text.
* Pre-recorded audio files in the `ticket-processing/data/` folder to use for testing the app.
* A `summarize.prompty` file where the prompt is constructed and edited.
* A `requirements.txt` file with all the python packages needed to run this example.
* Built-in evaluations to test your Prompt Flow against a variety of test datasets with telemetry pushed to Azure AI Studio
* You will be able to use this app with Azure AI Studio

### Architecture Diagram
![Architecture Digram](https://github.com/Azure-Samples/summarization-openai-python-promptflow/blob/main/images/architecture-diagram-summarization-aistudio.png)


### Demo Video 
(Embed demo video here)

## Getting Started

### Prerequisites

### Azure Account 

**IMPORTANT:** In order to deploy and run this example, you'll need:

* **Azure account**. If you're new to Azure, [get an Azure account for free](https://azure.microsoft.com/free/cognitive-search/) and you'll get some free Azure credits to get started. See [guide to deploying with the free trial](docs/deploy_lowcost.md).
* **Azure subscription with access enabled for the Azure OpenAI service**. You can request access with [this form](https://aka.ms/oaiapply). If your access request to Azure OpenAI service doesn't match the [acceptance criteria](https://learn.microsoft.com/legal/cognitive-services/openai/limited-access?context=%2Fazure%2Fcognitive-services%2Fopenai%2Fcontext%2Fcontext), you can use [OpenAI public API](https://platform.openai.com/docs/api-reference/introduction) instead. Learn [how to switch to an OpenAI instance](docs/deploy_existing.md#openaicom-openai).
* **Azure account permissions**:
  * Your Azure account must have `Microsoft.Authorization/roleAssignments/write` permissions, such as [Role Based Access Control Administrator](https://learn.microsoft.com/azure/role-based-access-control/built-in-roles#role-based-access-control-administrator-preview), [User Access Administrator](https://learn.microsoft.com/azure/role-based-access-control/built-in-roles#user-access-administrator), or [Owner](https://learn.microsoft.com/azure/role-based-access-control/built-in-roles#owner). If you don't have subscription-level permissions, you must be granted [RBAC](https://learn.microsoft.com/azure/role-based-access-control/built-in-roles#role-based-access-control-administrator-preview) for an existing resource group and [deploy to that existing group](docs/deploy_existing.md#resource-group).
  * Your Azure account also needs `Microsoft.Resources/deployments/write` permissions on the subscription level.


Once you have an Azure account you have two options for setting up this project. The easiest way to get started is GitHub Codespaces, since it will setup all the tools for you, but you can also set it up [locally]() if desired.

### Github Codespaces 

You can run this repo virtually by using GitHub Codespaces, which will open a web-based VS Code in your browser:
[Github Codespaces](https://codespaces.new/Azure-Samples/summarization-openai-python-promptflow)

### Local Environment 

- Install [azd](https://aka.ms/install-azd)
    - Windows: `winget install microsoft.azd`
    - Linux: `curl -fsSL https://aka.ms/install-azd.sh | bash`
    - MacOS: `brew tap azure/azd && brew install azd`
- [Python 3.9, 3.10, or 3.11](https://www.python.org/downloads/)
    Important: Python and the pip package manager must be in the path in Windows for the setup scripts to work.
    Important: Ensure you can run python --version from console. On Ubuntu, you might need to run sudo apt install python-is-python3 to link python to python3.
- [Node.js 14+](https://nodejs.org/en/download/) 
- [Git](https://git-scm.com/downloads)
- [Powershell 7+ (pwsh)](https://github.com/powershell/powershell) - For Windows users only.
    Important: Ensure you can run pwsh.exe from a PowerShell terminal. If this fails, you likely need to upgrade PowerShell.
- This sample uses `gpt-3.5-turbo` and [OpenAI text to speech models](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models#text-to-speech-preview) which may not be available in all Azure regions. Check for [up-to-date region availability](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#standard-deployment-model-availability) and select a region during deployment accordingly
    - We recommend using `swedencentral`for Azure OpenAI and `eastus` for the speech to text services 
 
### Installation 

To install the neccessary python dependencies navigate to the root directory and run the following command.
```
pip install -r requirements.txt
```
### Quickstart
 
1. Clone the repository and intialize the project: 
```
azd init summarization-openai-python-promptflow
```
Note that this command will initialize a git repository, so you do not need to clone this repository.

2. Login to your Azure account:
```
azd auth login
```

3. Create a new azd environment:
```
azd env new
```
Enter a name that will be used for the resource group. This will create a new folder in the .azure folder, and set it as the active environment for any calls to azd going forward.

4. Provision and deploy the project to Azure: `azd up`
6. Set up CI/CD with `azd pipeline config`
7. To run the sample navigate into the the correct folder by running `cd speech-recognition`. 
8. Run `python speech_to_text.py` to use the app with the sample audio data.  

### Local Development
Describe how to run and develop the app locally

## Costs
You can estimate the cost of this project's architecture with [Azure's pricing calculator](https://azure.microsoft.com/pricing/calculator/)
 
- Azure OpenAI: Standard tier, GPT and Ada models. Pricing per 1K tokens used, and at least 1K tokens are used per question. [Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/)
- Azure AI Speech: Pay as you go, Standard,	$1 per hour [Pricing](https://azure.microsoft.com/en-gb/pricing/details/cognitive-services/speech-services/)


## Securtiy Guidelines

We recommend using keyless authentication for this project. Read more about why you should use managed identities on our [blog](https://techcommunity.microsoft.com/t5/microsoft-developer-community/using-keyless-authentication-with-azure-openai/ba-p/4111521). 

## Resources

- For more information about working with Prompty and Prompt Flow, read the docs [here](https://microsoft.github.io/promptflow/how-to-guides/develop-a-prompty/index.html)
- [azure-search-openai-demo](https://github.com/Azure-Samples/azure-search-openai-demo?tab=readme-ov-file)
- [Develop Python apps that use Azure AI services](https://learn.microsoft.com/azure/developer/python/azure-ai-for-python-developers)



## UPDATED COMMANDS
pf flow test --flow ./summarizationapp --inputs problem="data/audio-data/issue0.wav"
pf flow test --flow ./summarizationapp --inputs problem="I need to open a problem report for part number ABC123. The brake rotor is overheating causing glazing on the pads. We track temperature above 24 degrees Celsius and we are seeing this after three to four laps during runs when the driver is braking late and aggressively into corners. The issue severity is to be prioritized as a 2. This is impacting the front brake assembly EFG234"
