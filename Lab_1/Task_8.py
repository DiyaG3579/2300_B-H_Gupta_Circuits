def truncate (number, decimal):
    factor = 10**decimal
    return int(number*factor)/factor
print(truncate(3.141596,4))