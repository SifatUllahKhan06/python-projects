import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
User_choice = int(input("What do you choose?\nType 0 for Rock...\nType 1 for Paper...\nType 2 for Scissors...\n"))
if User_choice>=3 or User_choice<0:
    print("Please Type Correct Number")
else:
    game_images = [rock,paper,scissors]
    print(game_images[User_choice])
    Computer_choice = random.randint(0,2)
    print(f"Computer Choice: {Computer_choice}")
    print(game_images[Computer_choice])
    if User_choice == 0 and Computer_choice == 1:
        print("You Loose...")
    elif User_choice == 1 and Computer_choice == 2:
        print("You Loose...")
    elif User_choice == 2 and  Computer_choice == 0:
        print("You Loose")
    elif User_choice == 0 and Computer_choice == 2:
        print("You Win!!!")
    elif User_choice == 1 and Computer_choice == 0:
        print("You Win!!!")
    elif User_choice == 2 and Computer_choice == 1:
        print("You Win...")
    elif User_choice == Computer_choice :
        print("Its a Draw ###")
