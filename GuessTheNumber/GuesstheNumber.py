import random

def guess(x):
    random_numnber = random.randint(1, x)
    guess = 0
    while guess != random_numnber:
        guess = int(input(f"input a number between 1 and {x}: "))
        if guess > random_numnber:
            print(f"You nuumber is too large guess agian")
        elif guess < random_numnber:
            print(f"your number is too low guess agian")

    print(f"you guessed the right number {random_numnber}")


def computer_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} the number? too high(h), too low(l), correct(c)").lower()
        if feedback == "h":
            high = guess -1
        elif feedback == "l":
            low = guess +1

    print(f"the number is {guess}")





computer_guess(100)
