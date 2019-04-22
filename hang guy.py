import random

Easy_Words = ["square", "subtract", "destroy", "section", "aardvark"]
Medium_Words = ["computation", "addition", "attrition", "fidelity", "hackathon"]
Hard_Word = ["supercalifragilisticexpialidocious"]

def main():
    Difficulty = input["choose ur difficulty: easy, medium, or hard "]
    if Difficulty == "easy"
        easymode()
    elif Difficulty == "medium"
    
    else Difficulty == "hard"


def easymode()
    RandoNando = random.randint(0,4)
    easyWord = Easy_Words[RandoNando] #this is the word user must guess
    easyLength = len(easyWord)        #this is the number of letters users must guess
    print('you have 6 tries. the number of words u need ',easyLength)
    tries = 6
    while tries != 0:
        attempt = input("enter letter --> ") #user attempt at letter
        truevalue = easyWord.find(attempt)   #checking the user attempt against true word
    if truevalue == -1:
        tries = tries - 1
    else 
            
    
    
    
    
    
    
