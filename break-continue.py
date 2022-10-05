# from asyncore import loop
# break and continue are the keywords in python used to control loops
# 1. break
#      it is used to abort the further execution of the loop and enters out of the loop
# 2. continue
# The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.
table = 25
for i in range(1,25):
    if(i == 11):
        break
    print(table, "X", i , "=" , table*i)


print("using continue")
for i in range(1,25):
    if(i == 11):
        continue
    print(table, "X", i , "=" , table*i)

