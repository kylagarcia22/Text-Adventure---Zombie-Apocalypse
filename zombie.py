print ("It is the year 4051 and the world has been overran by zombies. You find yourself alone in the middle of nowhere. Your goal is to stay alive and make it out safely.")

def left():
    print("You walk along the path and enter the city. You meet a stranger who is willing to help you.")
def right():
    print("You walk along the path and enter a forest. You encounter a pack of wolves.")
def fight():
    print("You are too weak and the wolves end up eating you. You are dead.")
    print("GAME OVER")
def run():
    print ("You outrun the wolves and make it out safely.")
    print ("YOU WIN")
def yes():
    print("With their help, the two of you venture out and defeat the zombies.")
    print("YOU WIN")
def no():
    print("An ambush of zombies rushes towards you and you die.")
    print ("GAME OVER")

path = str(input("You explore the area and find a road split into two paths. Do you choose to go left or right?"))

if path == ("left") or ("Left"):
    left()

elif path == ("right") or ("Right"):
    right()

else:
    print ("Wrong input. Try again.")

forest = str(input("Do you want to fight or run?")

if forest == ("run") or ("Run"):
    run()
elif forest == ("fight") or ("Fight"):
    fight()

else:
    print("Wrong input. Try again.")

city = str(input("Do you let them join you?"))

if city == ("yes") or ("Yes"):
    yes()
elif city == ("no") or ("No"):
    no()

else:
    print("Wrong input. Try again.")
