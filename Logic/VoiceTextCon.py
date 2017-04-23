import os
import json
from os.path import join, dirname
# from dotenv import load_dotenv
from watson_developer_cloud import SpeechToTextV1 as SpeechToText
import scipy.io.wavfile as wavfile
#from recorder.recorder import Recorder
import wave


def VoicetoTextConv(audio_file_input):
     try:

         stt = SpeechToText(
                # username=os.environ.get("STT_USERNAME"),
                 # password=os.environ.get("STT_PASSWORD"))
                 username="a56b6768-f396-4aa3-9c1b-38f516c04767",
                 password="FTobWRrz4KOO")

         print("Transcribing audio....\n")
         output_result = stt.recognize(audio_file_input,content_type='audio/wav')
         output_text = output_result['results'][0]['alternatives'][0]['transcript']
         print("Text: " + text + "\n")

     except:
       print("IOError detected, restarting...")


       return output_text



if __name__ == '__main__':

    rate, data = wavfile.read("speech.wav")
    VoicetoTextConv(data)
    
