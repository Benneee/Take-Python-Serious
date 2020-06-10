from sys import exit
from dead import dead
from start import start

def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number")
    
    if how_much < 50:
        print("Nice, you're not greedy, you win")
        exit(0)

    else:
        dead("You greedy bastard")



def bear_room():
    print("There is a bear here.")
    print("THe bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    
    bear_moved = False

    while True:
        print("Here are your options: ")
        print("1. take honey")
        print("2. taunt bear")
        print("3. open door")
        print("Type only the text of your chosen option in the prompt below")

        choice = input("> ")

        if choice == "take honey":
            dead("The bear looks at you then slaps your face off")
        
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now")
            bear_moved = True
        
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")

        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you go flee for your life or eat your head?")

    print("Here are your options: ")
    print("1. flee")
    print("2. head")
    print("Type only the text of your preferred option in the prompt below")

    choice = input("> ")

    if "flee" in choice:
        # direction = start()
        # if direction == "left":
        #     bear_room()
        # elif direction == "right":
        #     cthulhu_room()
        # else:
        #     dead("You stumble around the room until you starve")
        choose_direction()
    
    elif "head" in choice:
        dead("Well, that was tasty!")
    
    else:
        cthulhu_room()


def choose_direction():
    direction = start()
    if direction == "left":
        bear_room()
    elif direction == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

choose_direction()