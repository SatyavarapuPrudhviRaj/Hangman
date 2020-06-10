# Write your code here
import random

print('H A N G M A N')

word_list = ['python', 'java', 'kotlin', 'javascript']

chosen = random.choice(word_list)


tries = 0
hide = '-' * len(chosen)
attempted_letters = []

while True:
    dscn = input('Type "play" to play the game, "exit" to quit:')
    if dscn != 'play':
        break

    
    while tries < 8:
        print()
        print(hide)
        letters = input('Input a letter:')
        if letters in attempted_letters:
            print("You already typed this letter")
            # tries -= 1
            continue
        if len(letters) != 1 :
            print("You should input a single letter")
        #  tries -= 1
            continue
            
        if  not letters.islower():
            print("It is not an ASCII lowercase letter")
            # tries -= 1
            continue
        
        attempted_letters.append(letters)
        for index, letter in enumerate(chosen):
            if letter == letters:
                guessed = list(hide)
                guessed[index] = letters
                hide = ''.join(guessed)
        if letters not in hide:
            print('No such letter in the word')
            tries += 1
        elif attempted_letters.count(letters) > 1:
            print('No improvements')
            tries += 1
        elif hide == chosen:
            print()
            print(chosen)
            print('You guessed the word!')
            print('You survived!')
            break
        if tries == 8:
            print('You are hanged!')
            break
