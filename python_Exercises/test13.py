from urllib import request
import json

# r = request.urlopen("http://www.google.com")
# print(r.getcode())
# print(r.data())

url="http://official-joke-api.appspot.com/random_ten"
r2=request.urlopen(url)
data = r2.read()
print(data)
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

for joke in jokes:
    print(joke)

