"""spam = ['apples', 'bananas', 'tofu', 'cats']
Write a function that takes a list value as an argument and 
separated by comma and a space with 'and' inserted before the last item.
The function should be able to work with any list value passed to it"""

def comma_separated(list_argunemt):
    result = ""
    for i in range(len(list_argunemt) - 2):
        word = str(list_argunemt[i])
        result += word + ", "
    result += str(list_argunemt[-2]) + " and " + str(list_argunemt[-1])
    return result

spam = ['apples', 3.14 , 'tofu', 'cats']

print(comma_separated(spam))
