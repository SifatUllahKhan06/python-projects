print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
Bill = 0
if size == 'S':
    Bill += 15
elif size == 'M':
    Bill += 20
elif size == 'L':
    Bill += 25
else:
    print("You typed the wrong inputs.")

if  pepperoni == 'Y':
    if size == 'S':
        Bill +=2
    elif size == 'M':
        Bill +=3
    elif size == 'L':
        Bill +=3

if extra_cheese == 'Y':
    Bill +=1
print(f"Your final bill is: ${Bill}.")

