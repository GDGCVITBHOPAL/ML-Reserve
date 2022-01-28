from dotenv import load_dotenv
from datetime import datetime
import os


from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

# Import namespaces
import azure.cognitiveservices.speech as speech_sdk

global targetLanguage
targetLanguage = ''


def gui():

    # from tkinter import *
    # Explicit imports to satisfy Flake8

    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path("./assets")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    window = Tk()

    window.geometry("843x491")
    window.configure(bg="#FE724D")


    canvas = Canvas(
        window,
        bg="#FE724D",
        height=491,
        width=843,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: makeFR(targetLanguage),
        relief="flat"
    )
    button_1.place(
        x=591.6849365234375,
        y=53.99999999999994,
        width=214.3150634765625,
        height=186.14793395996094
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: makeES(targetLanguage),
        relief="flat"
    )
    button_2.place(
        x=359.0,
        y=53.99999999999994,
        width=214.3150634765625,
        height=186.14793395996094
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: makeHI(targetLanguage),
        relief="flat"
    )
    button_3.place(
        x=359.0,
        y=257.2931518554687,
        width=214.3150634765625,
        height=186.14793395996094
    )

    button_image_4=PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4=Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: makeDE(targetLanguage),
        relief="flat"
    )
    button_4.place(
        x=591.6849365234375,
        y=257.2931518554687,
        width=214.3150634765625,
        height=186.14793395996094
    )

    canvas.create_rectangle(
        37.0,
        40.99999999999994,
        306.0,
        442.99999999999994,
        fill="#FFFFFF",
        outline="")

    button_image_5=PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5=Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: makeqt(targetLanguage),
        relief="flat"
    )
    button_5.place(
        x=57.0,
        y=383.99999999999994,
        width=230.0,
        height=39.0
    )
    canvas.create_text(
    54.0,
    70.99999999999994,
    anchor="nw",
    text="Captraduire",
    fill="#8A00BB",
    font=("Comfortaa Regular", 34 * -1)
)

    canvas.create_text(
        60.0,
        360.99999999999994,
        anchor="nw",
        text="  to End the program, click below\n",
        fill="#000000",
        font=("Comfortaa Regular", 13 * -1)
    )

    canvas.create_text(
        58.0,
        207.99999999999994,
        anchor="nw",
        text="Instructions :",
        fill="#6D6D6D",
        font=("FontAwesome5Brands Regular", 15 * -1)
    )

    canvas.create_text(
        61.0,
        217.99999999999994,
        anchor="nw",
        text="",
        fill="#6D6D6D",
        font=("FontAwesome5Brands Regular", 15 * -1)
    )

    canvas.create_text(
        75.0,
        269.99999999999994,
        anchor="nw",
        text="∘ Speak in English",
        fill="#6D6D6D",
        font=("FontAwesome5Brands Regular", 15 * -1)
    )

    canvas.create_text(
        75.0,
        324.99999999999994,
        anchor="nw",
        text="∘ You're good to go",
        fill="#6D6D6D",
        font=("FontAwesome5Brands Regular", 15 * -1)
    )

    canvas.create_text(
        75.0,
        235.99999999999994,
        anchor="nw",
        text="∘ Click on the desired",
        fill="#6D6D6D",
        font=("FontAwesome5Brands Regular", 15 * -1)
    )

    canvas.create_text(
        75.0,
        249.99999999999994,
        anchor="nw",
        text="    language button",
        fill="#6D6D6D",
        font=("FontAwesome5Brands Regular", 15 * -1)
    )

    canvas.create_text(
        75.0,
        290.99999999999994,
        anchor="nw",
        text="∘ Wait for the program to",
        fill="#6D6D6D",
        font=("FontAwesome5Brands Regular", 15 * -1)
    )

    canvas.create_text(
        75.0,
        305.99999999999994,
        anchor="nw",
        text="   translate",
        fill="#6D6D6D",
        font=("FontAwesome5Brands Regular", 15 * -1)
    )

    canvas.create_text(
        60.0,
        125.99999999999994,
        anchor="nw",
        text="Welcome to Captraduire,",
        fill="#FE724D",
        font=("Comfortaa Regular", 18 * -1)
    )

    canvas.create_text(
        60.0,
        146.99999999999994,
        anchor="nw",
        text="your on the go",
        fill="#FE724D",
        font=("Comfortaa Regular", 18 * -1)
    )

    canvas.create_text(
        60.0,
        167.99999999999994,
        anchor="nw",
        text="translator.",
        fill="#FE724D",
        font=("Comfortaa Regular", 18 * -1)
    )
    window.resizable(False, False)
    window.mainloop()



def main(targetLanguage):
    try:
        global speech_config
        global translation_config

        # Get Configuration Settings
        load_dotenv()
        cog_key=os.getenv('COG_SERVICE_KEY')
        cog_region=os.getenv('COG_SERVICE_REGION')

        # Configure translation
        translation_config=speech_sdk.translation.SpeechTranslationConfig(
            cog_key, cog_region)
        translation_config.speech_recognition_language='en-US'
        translation_config.add_target_language('fr')
        translation_config.add_target_language('es')
        translation_config.add_target_language('hi')
        translation_config.add_target_language('de')
        print('ready to translate from',
              translation_config.speech_recognition_language)

        # Configure speech
        speech_config=speech_sdk.SpeechConfig(cog_key, cog_region)

        # Get user input
        targetLanguag=''
        while targetLanguag != 'quit':
            targetLanguag=gui()

    except Exception as ex:
        print(ex)

def makeFR(targetLanguage):
    targetLanguage="fr"
    Translate(targetLanguage)
    return targetLanguage


def makeES(targetLanguage):
    targetLanguage="es"
    Translate(targetLanguage)
    return targetLanguage


def makeHI(targetLanguage):
    targetLanguage="hi"
    Translate(targetLanguage)
    return targetLanguage


def makeDE(targetLanguage):
    targetLanguage="de"
    Translate(targetLanguage)
    return targetLanguage


def makeqt(targetLanguage):
    return exit()

def Translate(targetLanguage):
    translation=''

    # Translate speech
    audio_config=speech_sdk.AudioConfig(use_default_microphone=True)
    translator=speech_sdk.translation.TranslationRecognizer(
        translation_config, audio_config)
    print("Speak now...")
    result=translator.recognize_once_async().get()
    print(f'Translating {result.text}')
    translation=result.translations[targetLanguage]
    print(translation)

    # Synthesize translation
    voices={
        "fr": "fr-FR-DeniseNeural",
        "es": "es-ES-AlvaroNeural",
        "hi": "hi-IN-MadhurNeural",
        "de": "de-DE-KatjaNeural"
    }
    speech_config.speech_synthesis_voice_name=voices.get(targetLanguage)
    speech_synthesizer=speech_sdk.SpeechSynthesizer(speech_config)
    speak=speech_synthesizer.speak_text_async(translation).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)


if __name__ == "__main__":
    main(targetLanguage)
