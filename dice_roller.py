import random
import time

def dice_roll():
    return random.randint(1,6)

my_dice=['⚂', '⚁', '⚄', '⚀', '⚃']

def count_down():
    print('Rolling the dice ',end='')
    for _ in range(3):
        dice=random.choice(my_dice)
        print(dice,end=" ",flush=True)
        time.sleep(0.5)
    print()

while True:
    input("Press Enter to roll the dice (or type 'q' and press Enter to quit):")
    count_down()
    res=dice_roll()
    print(f"You rolled a Number: {res}! 🎉🎲\n")

    cnt=input('Wanna Roll Again!(y/n)').lower()
    if cnt != 'y':
        print('Thanks for Rolling..:)')
        break

