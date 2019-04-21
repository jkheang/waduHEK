import random

def main():
    guessthenumber = input("guess a number between 1 and 30: ")
    theNumber = numbergenerator()
    if guessthenumber == theNumber:
        print('you got it')
    else:
        gamestart = input('nope, would you like to try again ')
        if gamestart == "yes":
            print('good job ')
            main()
        if gamestart == "no":
            print("later loser ")
    
def numbergenerator():
    theNumber = random.randint(1,30)
    return theNumber

if __name__ == "__main__":
    main()
