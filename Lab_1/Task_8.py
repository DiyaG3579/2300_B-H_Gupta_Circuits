def truncate (number, decimal):
    factor = 10**decimal #Find the factor needed for the number of decimal places 
    return int(number*factor)/factor #Move the decimal, remove the extra digits, and then mmove the decimal back
print(truncate(3.141596,4))