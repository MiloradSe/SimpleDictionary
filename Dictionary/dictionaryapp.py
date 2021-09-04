import json
from difflib import get_close_matches


data = json.load(open("data.json"))

def define(word):
    word = word.lower()

    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        response = input("Did you mean %s? Enter(Y/N) " % get_close_matches(word, data.keys())[0])
        response = response.upper()
        if response == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif response == "N":
            return "Word you typed does not exist in this dictionary. "
        else:
            return "Your entry is not supported as an answer to the given question. "
    else:
        return "Word does not exist in the dictionary. Please double check it. "

word = (input("Type in word to translate: "))
output = define(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
