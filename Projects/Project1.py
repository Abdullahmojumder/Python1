name = input("Hey, type your name: ")
print("hello", name, "welcome to the game!")


should_we_play = input("Do you want to play?").lower()


if should_we_play == "yes" or should_we_play == "y":
    print("We are gonna play")

    direction = input("Do you want to go left or right?").lower()
    if direction == "left":
        print("You went left and fell off a cliff, game over.")
    elif direction == "right":
        choice = input("You saw a bridge, do you want to swim or cross it?")
        if choice == "swim":
            print("You got eaten by an alligator, the end")
        else:
            print("You found the gold and won!")
    else:
        print("Sorry, not a valid option.")

else:
    print("We are not playing...")
