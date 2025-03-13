import requests
import json
import win32com.client as wincom
city = input("Enter the name of the city\n")

url = f"http://api.weatherapi.com/v1/current.json?key=8ab8fcf128f94c93a0b61100250803&q={city}"

speak = wincom.Dispatch("SAPI.SpVoice")
# text = "wdic"
r = requests.get(url)
# print(r.text)
wdic = json.loads(r.text)
l = wdic["location"] ["country"]
w = wdic["current"]["temp_c"]
u = wdic["current"]["temp_f"]
f = wdic["location"] ["localtime"]
speak.Speak(f"The current weather in {city} location of {l} is {w} & {u} degrees and localtime is {f}  ")