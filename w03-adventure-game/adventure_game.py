"""
Author : ASILATSA DOUNYA BRANDON
Prupose: W03 Project-Adventure Game

Extra: I added multiple levels of choices so each decision leads to a different outcome.
"""

print("You wake up in a strange dark room with two doors in front of you, each door with something written on each of it.")
print("One door has PEACE written on it and the other has FREEDOM")

choice = input("Which door do you choose? (PEACE / FREADOM) ").lower()

if choice == "peace":
    print("\nYou open the peace door and feel a strong heat coming from inside.")
    second_choice = input("Do you want to Enter or GO BACK? (ENTER / GO BACK) ").lower()

    if second_choice == "enter":
        print("You step inside and see fire everywhere.")
        third_choice = input("Do you want to RUN or FACE the fire? (RUN / FACE) ").lower()

        if third_choice == "run":
            print("You escape safely, but you will always wonder what is inside.")
        elif third_choice == "face":
            print("The fire consumes you. Something peace is not what it seems.")
        else:
            print("Invalid choice. You hesitate too long and retreat.")

    elif second_choice == "go back":
        print("You return to the dark room, feeling not sure of your decision.")
    else:
        print("Invalid choice. You remain frozen in fear.")

elif choice == "freedom":
    print("You open the FREEDOM door and find a long quiet hallway.")
    second_choice = input("Do you want to WALK forward or LOOK around? (WALK / LOOK) ").lower()

    if second_choice == "walk":
        print("You walk forword and see an angel shinning at the end.")
        third_choice  = input("Do you want to FOLLOW the abgel or TURN BACK? (FOLLOW / TURN BACK) ").lower()

        if third_choice == "follow":
            print("You reach to him and he carries you to true freedom. You win.")
        elif third_choice == "turn back":
            print("You turn back and the door closes forever behind you.")
        else:
            print("Invalid choice. You stand still until the angel desappears.")

    elif second_choice == "look":
        print("You look around and discover hiddem symbols on the wall.")
        print("It is writen GOD IS YOUR SAVIOUR.")
    else: 
        print("Invalid choice. You wait, unsure of what to do.")

else:
    print("That is not valid choice. You stand till, unsure of what to do.")                                  

   
