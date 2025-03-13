import win32com.client as wincom

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.0 . ") 
    while True:
        speak = wincom.Dispatch("SAPI.SpVoice")
        x = input("Enter what you want me to pronounce : ")
        if x == "end":
            speak.Speak ("Bye bye friend")
            break
        command = speak.Speak(f" {x} ")
        



