import json
from difflib import get_close_matches
data = json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
       return data[word]
    elif word.title() in data: #if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        ok = input("Did you mean %s instead? Enter Y is Yes, or N if No." %get_close_matches(word,data.keys())[0])
        if ok =="Y" or ok =="y":
            return data[get_close_matches(word,data.keys())[0]]
        elif ok=="N" or ok=="n":
            return "The Word doesn't exist. Please double check it."
        else:
            return "We didn't understand your entry"
    else :
        return "The Word doesn't exist! Please Double check it"

word = input("Enter Word: ")

output = translate(word)
if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)
