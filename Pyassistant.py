# from gtts import gTTS (google text to speech)
import win32com.client                    # python library for text to speech conversion
import speech_recognition as sr

listening = True


def response(command):
    audio = win32com.client.Dispatch("SAPI.SpVoice")
    # Dispatch method when passed with the argument of SAPI.SpVoice It interacts with the Microsoft Speech SDK to speak

    global listening
    if command in 'stop running':
        listening = False
        audio.speak('Ok stopping')
    elif 'how are you' in command:
        audio.speak('I am good  How you doin')
        print('I am good, How you doin')
    elif ('hello' in command) or ('hey' in command):
        audio.speak('hello how can i help you')
        print('hello how can i help you')


# initialising the recognizer

r = sr.Recognizer()  # instance of Recognizer has various speech recognition functionality.

while listening:
    try:
        # using system microphone as speech source and obtaining voice from it
        with sr.Microphone() as source:
            print('Microphone on...')

            r.adjust_for_ambient_noise(source, duration=0.5)

            audio = r.listen(source)  # listening voice of speaker

            # using google recognizer to extract text from audio
            text = r.recognize_google(audio)
            text = text.lower()
            response(text)
    except sr.UnknownValueError:
        print('', end='')
    except sr.RequestError as e:
        print(e)