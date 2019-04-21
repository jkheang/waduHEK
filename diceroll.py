import random
game_start = input("would u like to roll the dice?")

def dice_roll():
    print("ur number is" + str(random.randint(1,6)))
    global play_again
    play_again = input("would u like to play again?")

if game_start == "yes":
    dice_roll()
    while play_again == "yes":
        dice_roll()
elif game_start == "no":
    print("game over nerd")
    else:
        print("input bad")
        
    
    
        
