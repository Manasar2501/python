
from enum import Flag

#syntax
# if(boolen expression 1):
#     if boolen expression is true, then ececute this block of code
# elif(boolen expreesion 2):
#     if boolen expression 1 is false and boolen expression 2 is true, then ececute this block of code
# else:
#     if both are false, execute this block of code


num = 45

if(num < 0):
    print("the number is negative number")
elif(num <= 100 and num >50 ):
    print("entered number lies between 51 to 100")
elif(num <= 50 and num >0 ):
    print("entered number lies between 1 to 50")
else:
    print("entered number is greater than 100")