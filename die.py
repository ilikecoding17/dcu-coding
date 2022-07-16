import random

list = ["one", "two", "three", "four", "five", "six"]			# List
list2 = ["heads", "tails"]
item2 = random.choice(list2)
item = random.choice(list)						# Chooses from list
dice = float(input("to roll dice, press 2, to flip coin, press 1 "))
if dice == 1 :
  print (item)
elif dice == 2 :
  print (item2)