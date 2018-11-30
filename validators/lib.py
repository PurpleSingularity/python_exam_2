
"""
    Написати валідатор ....
    Правило валідації
    xx-444-1
"""

import re

def getUserPasCode():

    user_input = input('')

    if (re.match(r"(\W{2}),(-),(\d{3}),(-),(\d{1})", user_input) ):
        return user_input
    else:
        return False


"""
    Написати валідатор ....
    Правило валідації
    Слова, одне або декілька, з велкої літери
"""

def getCountryName():
    user_input = input('')

    if (re.search(r"/w+", user_input) ):
        return user_input
    else:
        return False



"""
    Написати валідатор ....
    Правило валідації
    1111.11' ''usd'
"""


def getMoney():
    user_input = input('')

    if (re.match(r"(/d{1-4},/.,/d{1-2}), ,usd", user_input) ):
        return user_input
    else:
        return False