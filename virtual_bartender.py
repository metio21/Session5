from random import choice
drinks = ["gin", "vodka", "eiskey", "rum", "tequila", "absinthe", "sake"]
print(choice(drinks))
name = input("I am the virtual bartender. What is your name? ")
legal = False
try:
    age = input("What is your age? ")
    age = int(age)
    country = input("What country are you from? ")
    legal = False
    if age >= 21:
        legal = True
    elif age >= 18 and (country != "USA" and country != "UAE"):
        legal = True
    elif age >= 16 and country == "Luxembourg":
        legal = True
except ValueError:
    print("Don't play game with me ")

#outside the except
if legal:
    print("It's my pleasure to serve you", choice(drinks))
else:
    print("Dear", name, "Unfortunately I can't serve you")
