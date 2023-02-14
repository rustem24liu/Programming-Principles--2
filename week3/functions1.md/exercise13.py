def guess_game():
    answer = 6
    cnt  = 0
    name = (input("Hello! What is your name?\n"))
    print()
    print("Well,", name+",", "I am thinking of a number between 1 and 20.")
    number = int(input("Take a guess.\n"))
    while number != answer:
        if number > answer:
            number = int(input("Your guess is too much!\n"))
            cnt+=1
        elif number < answer:
            number = int(input("Your guess is too low!\n"))
            cnt+=1
    else:
        print("Good job, KBTU! You guessed my number in", cnt, "guesses!")


guess_game()