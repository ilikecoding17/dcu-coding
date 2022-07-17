from tkinter import N


sum = float(input("this is the calculator. to add, type 1. to minus type 2. to multiply type 3. to divide type 4 \n "))
if sum == 1:
  add1 = float(input("please enter your first number  "))
  add2 = float(input("please enter your second number  "))
  addition = add1 + add2
  print("addition =", addition)

elif sum == 2:
  min1 = float(input("please enter your first number  "))
  min2 = float(input("please enter your second number  "))
  minus = min1 - min2
  print("subtraction =", minus)

elif sum == 3:
  mul1 = float(input("please enter your first number  "))
  mul2 = float(input("please enter your second number  "))
  multi = mul1 * mul2
  print("multiplication =", multi)

elif sum == 4:
  div1 = float(input("please enter your first number  "))
  div2 = float(input("please enter your second number  "))
  divide = div1 / div2
  print("division =", divide) 

else :
  print("sorry there was an error, print only the number 1, 2, 3, or 4 as said in the instructions")
  
  # this is a very cool comment yeah?