secret_number = 9
guess_count = 0
guess_limit = 5
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print('perfect you won!')
        break
else:
    print('Sorry, you failed maybe next time')

