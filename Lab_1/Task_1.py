#Importing everything that I need
import math

#Setting up the variables that will come into play - and establishing what x is (For the number of tires)
pi = 3.141592
r = float(input('Enter the Radius of Your Sphere: '))
x = 1

#Adding instructions and input
print('Press 1 to Calculate Surface Area; Press 2 to Calculate Volume')
quantity = int(input('What would you like to calculate: '))

#Loop to make sure they input something correctly
while x < 4:
    if quantity == 1:
        area = (4 * pi * r * r)
        print('Surface Area: ', area)
        x = 4
    elif quantity ==2:
        volume = (4 * pi * r * r)/3
        print('Volume: ', volume)
        x = 4
    else: 
        quantity = int(input('Please select 1 or 2 - (1 for Surface Area and 2 for Volume): '))
#Exiting out the code
if x >= 4:
    print('You have reached the maximum number of attempts, please try again by re-running the program')
