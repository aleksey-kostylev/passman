import random

def myrandpass():
    password = ''

    for x in range(15):
        password = password + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ'))
    
        if len(password) == 5:
            password += '-'
    
        if len(password) == 9:
            password += '-'

    print(f'Пароль {password} создан!')
    return password