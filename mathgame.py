import random
import string
import time

intro = True
points = 0
losses = 0
old_a = 0
old_b = 0
old_c = 0

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase

alphabet = lowercase + uppercase

print("This is a simple maths game. Welcome")


# The instructions thing gets kinda confusing, sorry for that
def instructions():
    print("\nValues between 1 and 10 will be displayed on your screen and you will\nhave to solve them as quickly as possible.")
    time.sleep(2)
    print("Answer correctly and you get a point, answer incorrectly 3 times and the game is\nover.")
    time.sleep(2)
    print("\nTry to get as high a score as possible")
    time.sleep(2)
    print("The game will start in: ")
    time.sleep(0.5)
    print("3")
    print("-")
    time.sleep(0.5)
    print("2")
    print("-")
    time.sleep(0.5)
    print("1")
    print("-")
    time.sleep(0.5)
    print("0")
    time.sleep(0.5)
    print("\n")
    time.sleep(0.25)
    print("-")
    print("\n")
    time.sleep(0.25)
    print("-")
    print("\n")
    time.sleep(0.25)
    print("-")
    print("\n")
    time.sleep(0.5)

    
print("Do you require instructions? ('Y/N')\n")
answer = input()

while intro:
    if answer == "Y" or answer == "y":
        instructions()
        intro = False

    elif answer == "N" or answer == "n":
        print("\nOk then let's start")
        time.sleep(0.5)
        print("\n3")
        time.sleep(0.5)
        print("\n2")
        time.sleep(0.5)
        print("\n1")
        time.sleep(0.5)
        print("\ngo\n")
        time.sleep(0.5)
        
        intro = False

    else:
        print("That's an invalid option, please try again")
        answer = input()

game = True
start_time = time.time()

while game:

    if losses == 3:
        print("Oh no you lost, well at least you managed to get " + str(points) + " points!")
        game_time = time.time() - start_time
        game_time = round(game_time)
        print("Fun fact: You played the game for " + str(game_time) + " seconds!")
        break

    
    a = random.randint(2, 12)
    b = random.randint(2, 12)
    c = a * b
        
    # I neither wanted the answer for the previous question be the same, nor did I want both answers to be a multiple of 10
    if c == old_c or old_a == 10 or old_b == 10:
        a = random.randint(2, 12)
        b = random.randint(2, 12)
        c = a * b
        
    print(str(a) + " x " + str(b))
    
    answer = input()
    old_c = c

    # if you were to accidentally enter a letter instead of a number it would register register as incorrect (since -1 can never be an answer) instead of having an error occur
    if str(answer) in alphabet:
        answer = -1
    
    if int(answer) == c:
        points = points + 1
        print("Correct!")
        print("Points: " + str(points)+ "\n")

    if int(answer) != c:
        losses = losses + 1
        print("Incorrect!\n")

    

    
