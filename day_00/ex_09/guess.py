import getopt, random, sys

print( "This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!")

to_find = random.randint(1, 99)
nb_tries = 0
answer = ""
while answer != "exit":
    answer = input("What's your guess between 1 and 99?\n")
    if answer.isnumeric() and int(answer) < to_find:
        print("Too low!")
    elif answer.isnumeric() and int(answer) > to_find:
        print("Too high!")
    elif answer.isnumeric() and int(answer) == to_find:
        if to_find == 42:
            print("The answer to the ultimate question of life, the universe and everything is 42.")
        if nb_tries == 1:
            print("Congratulations! You got it on your first try!")
        else:
            print(f'Congratulations, you\'ve got it!\n You won in {nb_tries} attempts!')
    else:
        if answer != "exit":
            print("That's not a number.")
    nb_tries += 1
print("Goodbye!")
