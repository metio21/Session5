# you have three lives, you role a dice, if you het a 6 you win
# if you do not fet a 6, you lose 1 life

from random import randint

lives = 3
while True: #as long as I have more lives
    #roll the dice
    dice = randint(1,6)
    if dice == 6:
        print("You rolled a 6! You win!")
        break
    lives = lives - 1
    print("You rolled a", dice, "you have", lives, "left")
    if lives == 0:
        print("You lose")
        break

