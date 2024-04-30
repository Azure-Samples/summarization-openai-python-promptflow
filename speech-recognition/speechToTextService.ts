const fs = require("fs");
const sdk = require("microsoft-cognitiveservices-speech-sdk");
const { DefaultAzureCredential } = require("@azure/identity");


export async function SpeechToTextFromFile(file_path) {

    //const speechConfig = sdk.SpeechConfig.fromSubscription(process.env.SPEECH_KEY, process.env.SPEECH_REGION);
    // use Entra user MI auth instead of key
    // reference: https://learn.microsoft.com/en-us/azure/ai-services/speech-service/how-to-configure-azure-ad-auth?tabs=azure-cli%2Cportal&pivots=programming-language-csharp
    // https://github.com/microsoft/cognitive-services-speech-sdk-js/blob/e89846a774639bfb05e9550d4d759871790cf627/src/sdk/SpeechConfig.ts#L25
    const resourceId = process.env.SPEECH_RESOURCE_ID;
    const region = process.env.SPEECH_RESOURCE_REGION;

    const credential = new DefaultAzureCredential({ managedIdentityClientId: process.env.AZURE_CLIENT_ID });
    var accessToken = await credential.getToken("https://cognitiveservices.azure.com/.default");
    var authorizationToken = `aad#${resourceId}#${accessToken}`;
    const speechConfig =sdk.SpeechConfig.fromAuthorizationToken(authorizationToken, region);
    
    speechConfig.speechRecognitionLanguage = "en-US";
    let audioConfig = sdk.AudioConfig.fromWavFileInput(fs.readFileSync(file_path));
    let speechRecognizer = new sdk.SpeechRecognizer(speechConfig, audioConfig);

    await speechRecognizer.recognizeOnceAsync(result => {
        switch (result.reason) {
            case sdk.ResultReason.RecognizedSpeech:
                console.log(`RECOGNIZED: Text=${result.text}`);
                return result.text;
            case sdk.ResultReason.NoMatch:
                console.log("NOMATCH: Speech could not be recognized.");
                return "NOMATCH: Speech could not be recognized.";
            case sdk.ResultReason.Canceled:
                const cancellation = sdk.CancellationDetails.fromResult(result);
                console.log(`CANCELED: Reason=${cancellation.reason}`);

                if (cancellation.reason == sdk.CancellationReason.Error) {
                    console.log(`CANCELED: ErrorCode=${cancellation.ErrorCode}`);
                    console.log(`CANCELED: ErrorDetails=${cancellation.errorDetails}`);
                    console.log("CANCELED: Did you set the speech resource key and region values?");
                }
                // return cancelation reason and erro rinfo
                return `CANCELED: Reason=${cancellation.reason}`;
        }
        speechRecognizer.close();
    });
}