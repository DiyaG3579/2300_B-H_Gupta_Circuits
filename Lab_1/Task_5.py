#Importing math, because you know that is this task's whole point
import math

#Starting with e = 0, because x^0 = 1 will be the first term
e = 0
#Getting the code (The first term will be num = 0, so it will always run it one less than submitted)
number = int(input("How many terms would you like your approximation to be done with: "))
x = 0

#Then the whole thing, the actual calculations
while x < number:
    top = math.pow(1,x)
    bottom = math.factorial(x)
    e = e + (top/bottom)
    x = x + 1

#Finally returning an answer
print("e =", e)  