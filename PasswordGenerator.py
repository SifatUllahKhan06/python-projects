import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
Password = ""
L = 0
S = 0
N = 0
for i in range(0,nr_letters):
    L = random.randint(0,27)
    Password += letters[L]
for j in range(0,nr_symbols):
    S = random.randint(0,10)
    Password += numbers[S]
for k in range(0,nr_numbers):
    N = random.randint(0,(len(symbols)))
    Password += symbols[N]
PasswordList = list(Password)
random.shuffle(PasswordList)
Password = "".join(PasswordList)
print(f"Your final password is {Password}")

