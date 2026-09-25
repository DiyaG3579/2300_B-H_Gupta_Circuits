Total = 0
while True:
	user_input = input("Enter a number or 'q' to quit:") # Get user input
	if user_input == 'q': #If input is equal to 'q', break the loop
		break
	num = int(user_input)
	Total += num #Add the number to the total
print("Here is the sum of all numbers entered: ", Total ) #Print the total sum of all numbers entered
