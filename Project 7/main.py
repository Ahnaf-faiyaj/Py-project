# import speech_recognition as sr
# import pyttsx3
# import datetime
# import pywhatkit
# import wikipedia

# listener = sr.Recognizer()
# alexa = pyttsx3.init()
# voices = alexa.getProperty('voices')
# alexa.setProperty('voice', voices[1].id)


# def talk(text):
#     alexa.say(text)
#     alexa.runAndWait()


# def take_command():
#     try:
#         with sr.Microphone() as source:
#             print('listening...')
#             voice = listener.listen(source)
#             command = listener.recognize_google(voice)
#             command = command.lower()
#             if 'alexa' in command:
#                 command = command.replace('alexa', '')
#     except:
#         pass
#     return command


# def run_alexa():
#     command = take_command()
#     if 'time' in command:
#         time = datetime.datetime.now().strftime('%I:%M %p')
#         print(time)
#         talk('Current time is ' + time)
#     elif 'play' in command:
#         song = command.replace('play', '')
#         talk('playing ' + song)
#         pywhatkit.playonyt(song)
#     elif 'tell me about' in command:
#         look_for = command.replace('tell me about', '')
#         info = wikipedia.summary(look_for, 1)
#         print(info)
#         talk(info)
#     else:
#         pywhatkit.search(command)


# while True:
#     run_alexa()

# This code give by gtp

import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia

listener = sr.Recognizer()
alexa = pyttsx3.init()
voices = alexa.getProperty('voices')
alexa.setProperty('voice', voices[1].id)


def talk(text):
    alexa.say(text)
    alexa.runAndWait()


def take_command():
    while True:
        try:
            with sr.Microphone() as source:
                print('Listening...')
                voice = listener.listen(source)
                command = listener.recognize_google(voice).lower()
                print(f'Heard: {command}')
                if 'alexa' in command:
                    command = command.replace('alexa', '').strip()
                    return command
                else:
                    print("Waiting for 'alexa' keyword...")
        except Exception as e:
            print("Error:", e)

def run_alexa():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)
    else:
        pywhatkit.search(command)


while True:
    run_alexa()