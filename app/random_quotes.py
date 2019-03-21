import json
from random import randint

with open("quotes.json") as f:
    quotes = json.load(f)


def random_quote():
    i = randint(0, len(quotes)-1)
    return quotes[i]
