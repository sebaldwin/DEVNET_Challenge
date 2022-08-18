import requests
import json
url = "https://icanhazdadjoke.com/"
search_url = "https://icanhazdadjoke.com/search?term="
headers = {
  "Accept": "Application/json"
}
JokeSub = input("Please enter a subject for a joke, or press enter for a random joke: ")
if JokeSub == "":
  RandJoke = requests.request("Get", url, headers=headers)
  RJoke = RandJoke.json()
  print(RJoke["joke"])
else:
  JokeSub != ""
  SubJoke = requests.request("Get", search_url+JokeSub, headers=headers)
  SJoke = SubJoke.json()
  print(SJoke["results"][0]["joke"])