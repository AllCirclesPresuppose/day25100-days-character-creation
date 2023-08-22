import random

print("⚔️ Character Stats Generator ⚔️")


def rollDice(sides):
  rand = random.randint(1, sides)
  print("You rolled ", rand)

def createCharacter():
  name = input("Name your warrior: ")
  eightSide = random.randint(1,8)
  sixSide = random.randint(1,6)
  health = sixSide * eightSide
  print("Their health is: ", health, "hp")
  
again = "yes"

while again == "yes" or again == "y":
  howMany = int(input("how many sides?: "))
  rollDice(howMany)
  createCharacter()
  again = input("Roll again? ")