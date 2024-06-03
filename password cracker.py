from random import choice

password = input("password to crack: ")

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

characters = letters + numbers

guess = [''] * len(password)
while ''.join(guess) != password:
    for i in range(len(password)):
        if guess[i] != password[i]:
            guess[i] = choice(characters)
            break
    print(''.join(guess))

print("password guessed!")
