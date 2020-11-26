import json
# difflib and SequenceMatcher compares two texts and returns a floating point
from difflib import SequenceMatcher
# from difflib import get_close_matches returns most common words
from difflib import get_close_matches
from termcolor import colored

# create a data dictionary from data.json file
data = json.load(open('data.json','r'))

#creates a function to search for a word in a dictionary and return it
def getdata(word):
    word = word.lower()
    if word in data:
        return (data[word])
    elif word.title() in data:
        return (data[word.title()])
    elif word.upper() in data:
        return (data[word.upper()])
    elif len(get_close_matches(word,data.keys(),n=1,cutoff=0.75)) > 0:
        question = input(f'Your word is "{word.upper()}", maybe you meant "{get_close_matches(word,data.keys())[0].upper()}"? Please answer y or n : ')
        if question.lower() == 'yes' or question.lower() == 'y':
            print('\n')
            return data[get_close_matches(word,data.keys())[0]]
        elif question.lower() == 'n' or question.lower() == "no":
            return 'Sorry, you can try again\n'
        else:
            return f'Sorry i can`t understand your input "{question}"'
    else:
        return f'\nSorry, I don`t have any information about: {word}\n'



while True:
    print(f'\nEnter a word to find it`s meaning\nOr insert quit or exit to close the program\n'.upper())
    word = input(colored("Please insert a word: ",'green'))

    if word.lower() == 'quit' or word.lower() == 'exit':
        print('Thank you and good bye'.upper())
        break
    elif isinstance(getdata(word),str):
        print(colored(getdata(word),'blue'))
    else:
        for i in getdata(word):
            print(colored(i,'blue'))
