print("Welcome to happy fun game")
name = input("What is your name ")
age = input("what is your age ")
print("hello ", name, "you are ", age ," years old")

if int(age) >= 18:
    print(name, " you are old enough")

wants_to_play = input("Do you wnant to play? ").lower()

if wants_to_play == "yes":
    print("Lets play")

    ans = input("Are you going to go left or right?(left/right)").lower()

    if ans == "left":
        print("left")

    elif ans == "right":
        print("right")

    else: print("you suck dumbass")

else:
    print(name, " you are not old enough")
