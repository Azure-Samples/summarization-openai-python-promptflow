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
- azure-app-service
- azure
page_type: sample
urlFragment: azure-search-openai-demo
---

# Automated Ticket Processing using Azure AI

Samples in JavaScript, .NET, and Java. Learn more at https://aka.ms/azai.

---

## Table of Contents

-
-
-
-
-
-



In this sample we recieve issues reported by field and shop floor workers at a company called Contoso Manufacturing, a manufacturing company that makes car batteries. The issues are shared by the workers either live through microphone input or pre-recorded as audio files. We translate the input from speech to text and then use an LLM and Prompty/Promptflow to summarize the issue and return the results in a format we specify.

 
# Ticket Processing
This sample uses the **[Azure AI Speech Service](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/)** and **[Python SDk](https://learn.microsoft.com/en-us/azure/ai-services/speech-service/quickstarts/setup-platform?pivots=programming-language-python&tabs=macos%2Cubuntu%2Cdotnetcli%2Cdotnet%2Cjre%2Cmaven%2Cnodejs%2Cmac%2Cvscode)** to translate the users speech into text. It leverages **Azure OpenAI** to summarize the text and **Prompty/Prompt Flow** to manage and insert the prompt into our code, and to evaluate prompt/LLM performance.

By the end of deploying this template you should be able to:

 1. Describe what Azure AI Speech Service Python SDK provides.
 2. Explain prompt creation with Prompty/Prompt Flow. 
 3. Build, run, evaluate, and deploy, the summarization app to Azure.

## Features

This project template provides the following features:

**For Developers**
* A Prompty file where the prompt is constructed
* Built-in evaluations to test your Prompt Flow against a variety of test datasets with telemetry pushed to Azure AI Studio
* Deployment available via GitHub actions or Azure AI SDK
* ...
**For Users**
* A Summarization application (front-end integration needed?)


### Architecture Diagram
Include a diagram describing the application (DevDiv is working with Designers on this part)

### Demo Video (opitonal)
(Embed demo video here0

## Security

(Document security aspects and best practices per template configuration)

* ex. keyless auth

We can show how to set up keyless auth for the speech sdk with azd. More detailed info here: https://learn.microsoft.com/en-us/azure/ai-services/speech-service/role-based-access-control

```
#grant permissions using azd (this assigns a Cognitive Services User role)

az role assignment create \
        --role "f2dc8367-1007-4938-bd23-fe263f013447" \
        --assignee-object-id "$PRINCIPAL_ID" \
        --scope /subscriptions/"$SUBSCRIPTION_ID"/resourceGroups/"$RESOURCE_GROUP" \
        --assignee-principal-type User

```

## Getting Started

### Prerequisites

(ideally very short, if any)
 
- Install [azd](https://aka.ms/install-azd)
    - Windows: `winget install microsoft.azd`
    - Linux: `curl -fsSL https://aka.ms/install-azd.sh | bash`
    - MacOS: `brew tap azure/azd && brew install azd`
- OS
- Library version
- This model uses [MODEL 1] and [MODEL 2] which may not be available in all Azure regions. Check for [up-to-date region availability](https://learn.microsoft.com/azure/ai-services/openai/concepts/models#standard-deployment-model-availability) and select a region during deployment accordingly
    - We recommend using [SUGGESTED REGION]
 
*marlenes suggested region is swedencentral! US East was not working for speech sdk
- ...
### Installation

- pip install promptflow promptflow-tools azure-cognitiveservices-speech dotenv

### Quickstart
(Add steps to get up and running quickly)
 
1. Clone the repository and intialize the project: `azd init [name-of-repo]`
2. ...
3. Provision and deploy the project to Azure: `azd up`
4. Set up CI/CD with `azd pipeline config`
5. (Add steps to start up the sample app)

### Local Development
Describe how to run and develop the app locally

## Costs
You can estimate the cost of this project's architecture with [Azure's pricing calculator](https://azure.microsoft.com/pricing/calculator/)
 
- [Azure Product] - [plan type] [link to pricing for product](https://azure.microsoft.com/pricing/)

## Securtiy Guidelines

TODO: team will add the guidelines here for best security practices.

## Resources

(Any additional resources or related projects)
 
- Link to supporting information
- Link to similar sample
- [Develop Python apps that use Azure AI services](https://learn.microsoft.com/azure/developer/python/azure-ai-for-python-developers)
- ...


