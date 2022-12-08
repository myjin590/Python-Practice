import random

print('----PASSWORD GENERATOR----')

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&*().,?0123456789'

number = input('Amount of password to generate : ')
number = int(number)

length = input('Length of Password: ')
length = int(length)

print('\Your password: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords+= random.choice(chars)
    print(passwords)



