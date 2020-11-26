import mysql.connector
from mysql.connector import cursor
from difflib import get_close_matches
from termcolor import colored

connection = mysql.connector.connect(
user = 'ardit700_student',
password = 'ardit700_student',
host = '108.167.140.122',
database = 'ardit700_pm1database'
)

cursor = connection.cursor()

query = cursor.execute(f'SELECT * FROM Dictionary')
results = cursor.fetchall()

#function to create a set of keys to search a word
def set_create(par):
    myset = set()
    for key,value in par:
        myset.add(key)
    return myset

# def a function to create a query:
def my_query(word):
    query=cursor.execute(f"SELECT * FROM Dictionary WHERE Expression = '{word}'")
    result = cursor.fetchall()
    return result

# function to print out the result
def printing(result):
        for a,b in result:
            print(colored(b,'blue'))

# create a function to take users input and search for the value
def getdata(word,myset):
    word = word.lower()
    if word in myset:
        return word
    elif word.title() in myset:
        return word.title()
    elif word.upper() in myset:
        return word.upper()
    elif len(get_close_matches(word,myset,n=1,cutoff=0.75)) > 0:
        question = input(f'Your word is "{word}", maybe you meant "{get_close_matches(word, myset)[0]}"? Please answer y or n : ')
        if question.lower() == 'yes' or question.lower() == 'y':
            return get_close_matches(word, myset)[0]
        if question.lower() == 'no' or question.lower() == 'n':
            return 'Sorry, try again'
        else:
            return f'Sorry i can`t understand your input "{question}"'
    else:
        return f'Sorry, I don`t have any information about: {word}\n'



myset = set_create(results)

while True:

    word = input('Please insert a word or "quit" to close a program: ')
    if word == 'quit':
        break
    else:

        word = getdata(word, myset)
        if word.startswith(('Sorry')):
            print(word)
            continue
        else:
            myresult = my_query(word)

        printing(myresult)










