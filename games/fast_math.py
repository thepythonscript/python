from random import *

print ("Lets play fast math!")
score = 0
turns = 10

for x in range (0, turns):
    num1 = randint(1, 10)
    num2 = randint(1, 10)

    print("what is", num1, "+", num2, "?")
    answer = input()

    if int(answer) == (num1 + num2):
        score += 1
        print("That's correct! Your score is ",score)
        

    else:
        print ("Incorrect. Your score is ",score)

print ("Game over.  Your score is ",score ,"out of ", turns)
