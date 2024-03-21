# pip install google-generativeai pyttsx3 SpeechRecognition pyaudio

import google.generativeai as genai
import pyttsx3
import speech_recognition as sr

#Using Google Gemini API key, you would have to get this from https://aistudio.google.com/app/apikey

import secrets_file
gemini_api_secret_name = secrets_file.api_key
genai.configure(api_key=gemini_api_secret_name)

model = genai.GenerativeModel('gemini-pro')

#Initialize text-to-speech
engine = pyttsx3.init()

def transcribe_audio_to_text(filename):
    recognizer = sr.Recognizer()
    with sr.AudioFile(filename) as source:
        audio = recognizer.record(source)
    try:
        return recognizer.recognize_google(audio)
    except:
        print("Skipping Unknown error")

def generate_response(prompt):
    audio_text = prompt

    response = model.generate_content(audio_text)
    text = response.text
    text = text.replace("*","")
    return text

def speak_text(text):
    engine.say(text)
    engine.runAndWait()
    return


def main():
    #Wait for user to say "Alpha"
    print("Say 'Alpha' to start recording your question...")
    
    while True:
        with sr.Microphone() as source:
            recognizer = sr.Recognizer()
            audio = recognizer.listen(source, timeout=None)

            try:
                transcription = recognizer.recognize_google(audio)
                if transcription.lower().startswith("alpha"):
                    #Record Audio
                    filename = "input.wav"
                    print("Say your Question")
                    with sr.Microphone() as source:
                        recognizer = sr.Recognizer()
                        source.pause_threshold = 1
                        audio = recognizer.listen(source,phrase_time_limit=None,timeout=None)
                        with open(filename, "wb") as f:
                            f.write(audio.get_wav_data())
                        
                        #Transcribe audio to text
                        text = transcribe_audio_to_text(filename)
                        if text:
                            print(f"You said: {text}")

                            #Generate response using Google Gemini
                            response = generate_response(text)
                            print(f"Gemini says: {response}")

                            # Read response using text-to-speech
                            speak_text(response)
                            print("Say 'Alpha' to start recording your question...")

            except Exception as e:
                pass

if __name__ == "__main__":
    main()