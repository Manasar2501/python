# from platform import python_branch
# from sqlite3 import ProgrammingError
# from tkinter import Variable
# from typing import Iterable


# there are 2 loops in python
# 1. for 
# 2. while

# for loop syntax
# for iterators_Variable in iterables:
#     print(iterators_Variable)
# here iterators_Variable may be any Variablethat can be given by Programmer 
# iterables are those which are being in loop. ex: range, list, tuple, string,..

# while Syntax
# while(a true condition):
#     run the code if conditin is true


lst = ["a", "b", 1, 2]
for i in range(len(lst)):
    print(i, end = ".")
    print(lst[i])
    print("\n")
#  0r

for j in lst:
    print(j)

print("while loop")

k = 0
while(k<len(lst)):
    print(lst[k])
    k+=1