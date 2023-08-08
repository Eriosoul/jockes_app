import requests

class JokeGetter:
    def __init__(self):
        pass

    def get_joke(self):
        resource = requests.get("https://official-joke-api.appspot.com/random_joke")
        data = resource.json()
        setup = data["setup"]
        punchline = data["punchline"]
        return setup, punchline