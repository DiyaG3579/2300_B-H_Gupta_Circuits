import math

e = 0
number = int(input("How many terms would you like your approximation to be done with: "))
x = 0

while x < number:
    top = math.pow(1,x)
    bottom = math.factorial(x)
    e = e + (top/bottom)
    x = x + 1

print("e =", e)  