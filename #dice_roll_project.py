#dice_roll_project

import random
import time

choice= 'yes'

while choice== "yes" or choice== 'y':
    print("\nDICE IS ROLLING..")
    time.sleep(2)
    d1=random.randint(1,6)
    d2=random.randint(1,6)
    print("\nDICE 1 IS:",d1)
    print("\nDICE 2 IS:",d2)

    if(d1==d2):
        print("YOU HAD A PERFECT ROLL")
    time.sleep(1)
    choice=input("CONTINUE ROLLING THE DICE? say yes or no: ").lower()
print("THANKYOU FOR PLAYING")
