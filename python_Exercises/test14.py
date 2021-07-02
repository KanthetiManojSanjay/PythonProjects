import json
import requests
import pyttsx3

engine=pyttsx3.init()


url="http://official-joke-api.appspot.com/random_ten"

response=requests.get(url)
print(response.status_code)
data = response.text
jsonData = json.loads(data)
print(jsonData)

class Joke:

    def __init__(self,setup,punchline) -> None:
        self.setup=setup
        self.punchline=punchline

    def __str__(self) -> str:
        return f"setup {self.setup} punchline {self.punchline}"



jokes=[]
for j in jsonData:
    setup = j["setup"]
    punchline = j["punchline"]
    joke=Joke(setup,punchline)
    jokes.append(joke)
print(f"Got {len(jokes)} jokes")

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
for joke in jokes:
    print(joke)
    pyttsx3.speak("Setup")
    pyttsx3.speak(joke.setup)
    pyttsx3.speak("The punchline")
    pyttsx3.speak(joke.punchline)

