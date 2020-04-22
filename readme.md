#### Idea
1. An app where users have to create and save recordings for certain words. The speech recognotion happens and then it gives them a score or certain feedback for the word that was pronounced.

#### Link on how to record audio on a web browser
1. https://developer.mozilla.org/en-US/docs/Web/API/MediaStream_Recording_API/Using_the_MediaStream_Recording_API

#### Authentication creditals for Google Cloud Transcription 
In order to run recognizer_instance.recognize_google_cloud you will need authentication credentials with Google Cloud Translate. You will have to set up a Cloud Consule project and create a service account to download a private key. https://cloud.google.com/speech-to-text/docs/quickstart-client-libraries
You will need to save the path to the key in your bash_profile so if can be found by the cloud translater service.

#### Google Cloud Translation
Make sure google cloud translate is installed 
$ pip install google-cloud-translate==2.0.0

If you get this message, you need to go to the URL listed to enable the API to be used on this project:
    "message": "Cloud Translation API has not been used in project 245533158177 before or it is disabled. Enable it by visiting https://console.developers.google.com/apis/api/translate.googleapis.com/overview?project=245533158177 then retry. If you enabled this API recently, wait a few minutes for the action to propagate to our systems and retry.",
 

Google cloud python client library documentation
https://cloud.google.com/translate/docs/reference/libraries/v2/python

more helppful documentation
https://googleapis.dev/python/translation/latest/usage.html


# Getting audio files in html5
https://developers.google.com/web/fundamentals/media/recording-audio