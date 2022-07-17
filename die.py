import random

list = ["one", "two", "three", "four", "five", "six"]			# List
list2 = ["heads", "tails"]
list3 = ["red", "orange", "yellow", "green", "blue", "indigo", "purple", "pink", "white","black","grey"]
item2 = random.choice(list2)
item = random.choice(list)						# Chooses from list
item3 = random.choice(list3)
dice = float(input("to roll dice, press 1, to flip coin, press 2, to pick a random colour press 3 \n "))
if dice == 1 :
  print (item)
elif dice == 2 :
  print (item2)
elif dice == 3 :
  print (item3)