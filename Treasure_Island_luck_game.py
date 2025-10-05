print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
User_choice1 = input("Hi its all depends on your luck...\nYou are on a crossroad....Which way you want to go??Left or Right??")
if User_choice1 == 'Right':
    print("Ooops,Try your luck next time....Game Over!!!")
elif User_choice1 == 'Left':
    print("Congratulations...You successfully cleared your first step")
    User_choice2 = input("Now You have reached a beautiful river...\nWhich way you feel more comfortable to cross the river??Swim or Wait??")
    if User_choice2 == 'Swim':
        print("Ooops,Try your luck next time....Game Over!!!")
    elif User_choice2 == 'Wait':
        print("Congratulations...You successfully cleared your second step\nNow the final step!!!")
        User_choice3 = input("Now you see three color doors...\nWhich door will you prefer??Red,Yellow or Blue??")
        if User_choice3 == 'Red' or User_choice3 == 'Blue':
            print("Ooops,Try your luck next time....Game Over!!!")
        elif User_choice3 == 'Yellow':
            print("Finally you made it...Congratulations!!!You won this game")
        else:
            print("Please enter correct input as per question(input is case sensitive)")
    else:
        print("Please enter correct input as per question(input is case sensitive)")
else:
    print("Please enter correct input as per question(input is case sensitive)")