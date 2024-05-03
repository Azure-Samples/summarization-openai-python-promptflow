const fs = require("fs");
const sdk = require("microsoft-cognitiveservices-speech-sdk");


export async function SpeechToTextFromFile(file_path) {

    const speechConfig = sdk.SpeechConfig.fromSubscription(process.env.SPEECH_KEY, process.env.SPEECH_REGION);
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