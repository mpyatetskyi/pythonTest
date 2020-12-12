def sentence_check(phrase):
    i = phrase.capitalize()
    conditions = ('how','why','what')
    if phrase.lower().startswith(conditions):
        return f'{i}?'
    else:
        return f'{i}.'

mylist = []

while True:
    myinput = input('Please, enter someting:')
    if myinput == '\end':
        break
    else:
        mylist.append(sentence_check(myinput))


print(' '.join(mylist))