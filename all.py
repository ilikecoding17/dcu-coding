import random
password = 863
name = str(input("please enter your name "))
unlock = float(input("please enter your password "))
if unlock == password :
  print ("password correct")
  print ("hello,", name)
  command = float(input("what would you like to do, to see list of possible commands type in 10 "))
if command == 10 :
  print("this is a list of all the functions that are available, if you type in 1, you will get a calculator.   if you type in 2, you will get a dice/coin flipper.   if you type in 3, you will get an age finder. ")
if command == 1 :
  sum = float(input("this is the calculator. to add, type 1. to minus type 2. to multiply type 3. to divide, type 4. "))
if sum == 1:
  add1 = float(input("please enter your first number "))
  add2 = float(input("please enter your second number "))
  addition = add1 + add2
  print("addition", addition)

elif sum == 2:
  min1 = float(input("please enter your first number "))
  min2 = float(input("please enter your second number "))
  minus = min1 - min2
  print("subtraction", minus)

elif sum == 3:
  mul1 = float(input("please enter your first number "))
  mul2 = float(input("please enter your second number "))
  multi = mul1 * mul2
  print("multiplication", multi)

elif sum == 4:
  div1 = float(input("please enter your first number "))
  div2 = float(input("please enter your second number "))
  divide = div1 / div2
  print("division", divide)



if command == 2:
  list = ["one", "two", "three", "four", "five", "six"]			# List
list2 = ["heads", "tails"]
item2 = random.choice(list2)
item = random.choice(list)						# Chooses from list
dice = float(input("to roll dice, press 2, to flip coin, press 1 "))
if dice == 1 :
  print (item)
elif dice == 2 :
  print (item2)


if command == 3:
  birthyear = float(input("when were you born \n"))
currentyear = 2022
age = currentyear - birthyear
print("you are", age,"years old")
print("you turn 100 in", 100+birthyear)