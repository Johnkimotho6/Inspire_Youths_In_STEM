secret_number = 9
guess_count = 0
#guess_limit = 3
while guess_count < 3:
    guess = int(input("Guess: "))
    guess_count += 1
    if  guess == secret_number:
        print("You won")
        #use break atatement to terminate a loop
        break
else:
    print("Sorry you failed")

