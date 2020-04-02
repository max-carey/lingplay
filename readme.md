#### Idea
1. An app where users have to create and save recordings for certain words. The speech recognotion happens and then it gives them a score or certain feedback for the word that was pronounced.

#### Link on how to record audio on a web browser
1. https://developer.mozilla.org/en-US/docs/Web/API/MediaStream_Recording_API/Using_the_MediaStream_Recording_API

#### Authentication creditals for Google Cloud Transcription 
In order to run recognizer_instance.recognize_google_cloud you will need authentication credentials with Google Cloud Translate. You will have to set up a Cloud Consule project and create a service account to download a private key. https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries
You will need to save the path to the key in your bash_profile so if can be found by the cloud translater service.