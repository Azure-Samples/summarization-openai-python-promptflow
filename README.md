<!--
---
page_type: sample
languages:
  - azdeveloper
  - python
  - bicep
products:
  - azure
  - ai-services
  - azure-openai
urlFragment: summarization-openai-python-promptflow
name: Process Automation with Speech to Text and Summarization with Azure Container Apps (ACA)
description: This sample creates a web-based app that allows workers at a company called Contoso Manufacturing to report issues via text or speech.
---
-->

<!-- YAML front-matter schema: https://review.learn.microsoft.com/help/contribute/samples/process/onboarding?branch=main#supported-metadata-fields-for-readmemd -->

# Process Automation: Speech to Text and Summarization with Azure Container Apps (ACA)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Azure-Samples/summarization-openai-python-promptflow) [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/azure-samples/summarization-openai-python-promptflow)

This sample creates a web-based app that allows workers at a company called Contoso Manufacturing to report issues via text or speech. Audio input is translated to text and then summarized to hightlight important information and specifiy the department the report should be sent to.

## Table of Contents

- [Features](#features)
- [Azure account requirements](#azure-account-requirements)
- [Opening the project](#opening-the-project)
    - [GitHub Codespaces](#github-codespaces)
    - [VS Code Dev Containers](#vs-code-dev-containers)
    - [Local environment](#local-environment)
      - [Prerequisites](#prerequisites)
      - [Initializing the project](#initializing-the-project)
- [Deployment](#deployment)
- [Exploring the sample](#exploring-the-sample)
  - [Understanding the prompty file](#understanding-the-prompty-file)
  - [Testing the sample](#testing-the-sample)
- [Costs](#costs)
- [Security Guidelines](#security-guidelines)
- [Resources](#resources)
- [Code of Conduct](#code-of-conduct)

## Features

This project template provides the following features:

* [Azure AI Speech Service](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/) to translate the users speech into text.
* [Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/) to summarize the text
* [Prompty and Prompt Flow](https://microsoft.github.io/promptflow/how-to-guides/develop-a-prompty/index.html) to create, manage and evaluate the prompt into our code.
  
![Architecture Digram](images/summarization-aca.png)

## Azure account requirements

In order to deploy and run this example, you'll need:

* **Azure account**. If you're new to Azure, [get an Azure account for free](https://azure.microsoft.com/free/cognitive-search/) and you'll get some free Azure credits to get started. See [guide to deploying with the free trial](docs/deploy_lowcost.md).
* **Azure subscription with access enabled for the Azure OpenAI service**. You can request access with [this form](https://aka.ms/oaiapply). If your access request to Azure OpenAI service doesn't match the [acceptance criteria](https://learn.microsoft.com/legal/cognitive-services/openai/limited-access?context=%2Fazure%2Fcognitive-services%2Fopenai%2Fcontext%2Fcontext), you can use [OpenAI public API](https://platform.openai.com/docs/api-reference/introduction) instead.
    - Ability to deploy `gpt-35-turbo`
    - We recommend using Sweden Central or East US 2
* **Azure subscription with access enabled for [Azure AI Speech Service](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/)**

## Getting Started

You have a few options for setting up this project.
The easiest way to get started is GitHub Codespaces, since it will setup all the tools for you, but you can also [set it up locally](#local-environment).

### GitHub Codespaces

1. You can run this template virtually by using GitHub Codespaces. The button will open a web-based VS Code instance in your browser:
   
    [![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/Azure-Samples/summarization-openai-python-promptflow)

2. Open a terminal window.
3. Sign in to your Azure account:

    ```shell
    azd auth login
    ```

4. Provision the resources and deploy the code:

    ```shell
    azd up
    ```

    This project uses gpt-3.5-turbo which may not be available in all Azure regions. Check for [up-to-date region availability](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#standard-deployment-model-availability) and select a region during deployment accordingly.

5. Install the necessary Python packages:

    ```
    cd src
    pip install -r requirements.txt
    ```

Once the above steps are completed you can jump straight to [exploring the sample](#exploring-the-sample). 

### VS Code Dev Containers

A related option is VS Code Dev Containers, which will open the project in your local VS Code using the [Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers):

1. Start Docker Desktop (install it if not already installed)
2. Open the project:
   
    [![Open in Dev Containers](https://img.shields.io/static/v1?style=for-the-badge&label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/Azure-Samples/summarization-openai-python-promptflow.git)

3. In the VS Code window that opens, once the project files show up (this may take several minutes), open a terminal window.

Once you've completed these steps jump to [deployment](#deployment). 

### Local Environment

#### Prerequisites

* [Azure Developer CLI (azd)](https://aka.ms/install-azd)
* [Python 3.10+](https://www.python.org/downloads/)
* [Docker Desktop](https://www.docker.com/products/docker-desktop/)
* [Git](https://git-scm.com/downloads)

#### Initializing the project

Create a new folder and switch to it in the terminal, then run this command to download the project code:

    ```shell
    azd init -t summarization-openai-python-promptflow
    ```
    Note that this command will initialize a git repository, so you do not need to clone this repository.

## Deployment

Once you've opened the project in [Dev Containers](#vs-code-dev-containers), or [locally](#local-environment), you can deploy it to Azure.

1. Sign in to your Azure account:

    ```shell
    azd auth login
    ```

    If you have any issues with that command, you may also want to try `azd auth login --use-device-code`.

2. Provision the resources and deploy the code:

    ```shell
    azd up
    ```

3. Install the necessary Python packages:

    ```
    cd src
    pip install -r requirements.txt
    ```

    This project uses gpt-3.5-turbo which may not be available in all Azure regions. Check for [up-to-date region availability](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#standard-deployment-model-availability) and select a region during deployment accordingly.

## Exploring the sample

### Understanding the prompty file

This sample repository contains a summarize prompty file you can explore. In this sample we are telling the model to summarize the reports given by a worker in a specific format. 

The prompty file contains the following:
- The name, description and authors of the prompt
- configuration: Details about the LLM model including:
  - api type: chat or completion
  - configuration: connection type (azure_openai or openai) and environment variables
  - model parameters: max_tokesn, temperature and response_format (text or json_object)
- inputs: the content input from the user, where each input should have a type and can also have a default value
- outputs: where the output should have a type like string
- Sample Section: a sample of the inputs to be provided
- The prompt: in this sample we send add a system message as the prompt with context and details about the format. We also add in a user message at the bottom of the file, which consists of the reported issue in text format from our user. 

If you ran the provisioning step above correctly, all of the variables should already be set for you. You can edit the prompt to see what changes this makes to the summary created. 

### Testing the sample

This repository contains sample data to be able to test the project end to end. To run this project you'll need to pass in as input a reported issue to be summarized. You can pass this input as either a `.wav` file or a string of text. The `data/audio-data/` folder contains sample audio files for you to use or you can use the example string shown below. Below are the commands you can use in your terminal to run the project locally with promptflow.

Testing with sample audio data. Make sure you are in the `src` directory: 
``` bash
pf flow test --flow summarizationapp --inputs problem="data/audio-data/issue0.wav"
```

Testing with sample text data:
``` bash
pf flow test --flow summarizationapp --inputs problem="I need to open a problem report for part number ABC123. The brake rotor is overheating causing glazing on the pads. We track temperature above 24 degrees Celsius and we are seeing this after three to four laps during runs when the driver is braking late and aggressively into corners. The issue severity is to be prioritized as a 2. This is impacting the front brake assembly EFG234"
```

To understand how the code works look through the `summarize.py` file. 

## Guidance

### Costs

Pricing may vary per region and usage. Exact costs cannot be estimated.
You may try the [Azure pricing calculator](https://azure.microsoft.com/pricing/calculator/) for the resources below:

* Azure Container Apps: Pay-as-you-go tier. Costs based on vCPU and memory used. [Pricing](https://azure.microsoft.com/pricing/details/container-apps/)
* Azure OpenAI: Standard tier, GPT and Ada models. Pricing per 1K tokens used, and at least 1K tokens are used per question. [Pricing](https://azure.microsoft.com/pricing/details/cognitive-services/openai-service/)
* Azure Monitor: Pay-as-you-go tier. Costs based on data ingested. [Pricing](https://azure.microsoft.com/pricing/details/monitor/)

### Security Guidelines

This template uses [Managed Identity](https://learn.microsoft.com/entra/identity/managed-identities-azure-resources/overview) for authenticating to the Azure services used (Azure OpenAI, Azure PostgreSQL Flexible Server).

Additionally, we have added a [GitHub Action](https://github.com/microsoft/security-devops-action) that scans the infrastructure-as-code files and generates a report containing any detected issues. To ensure continued best practices in your own repository, we recommend that anyone creating solutions based on our templates ensure that the [Github secret scanning](https://docs.github.com/code-security/secret-scanning/about-secret-scanning) setting is enabled.

## Resources

* [Promptflow/Prompty Documentation](https://microsoft.github.io/promptflow/reference/python-library-reference/promptflow-core/promptflow.core.html?highlight=prompty#promptflow.core.Prompty)
* [Develop Python apps that use Azure AI services](https://learn.microsoft.com/azure/developer/python/azure-ai-for-python-developers)


## Code of Conduct

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).

Resources:

- [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/)
- [Microsoft Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/)
- Contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with questions or concerns


For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
