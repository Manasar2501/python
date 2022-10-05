#IDENTIFIER/VARIABLES
#There are 4 rules need to be followed to declare a variable
# 1. first character must be alphabet(a,b,c,d,...z,A,B,C,..Z) or underscore(_).
# 2. except first character, all characters may be low case, upper case, underscore or digit.
# 3. variables must not be specail case(!, @, # , %, ^, &,|) and no white space.
# 4. variables must not be any keywords.

#---------------------------------------------------------------------------------------------

#BUILD-IN DATA TYPES

# Text data Type:	    str
# Numeric data Types:	int, float, complex
# Sequence data Types:	list, tuple, range
# Mapping data Type:	dict
# Set data data s:	    set, frozenset
# Boolean Type:	        bool
# None data Type:	    None Type

#type is a keyword used to get the data type of any object.
#syntax:  type()

#string
#string is defined inside a qoutes(single/double/triple)
name  =  'python'
print(type(name))
print(type("hi, python"))

#int, float,complex
intNumber = 100
floatNumber = 100.00
complexNumber = 4+1j
print(type(intNumber))
print(type(floatNumber))
print(type(complexNumber))

#boolean data type
isAnumber = True
isNotNum = False
print(type(isAnumber))

#None data type
a = None
print(a, type(a))

#--------------------------------------------------------------------------------------------
#TYPE CONVERSION
#In python data type can be converted.
#but string cannot be converted into int,because a series of characters can never be a numberic.
#Syntax : str(), int(), float(), complex(), list(), tuple(),bool().
#inside the brakets, specify the aurguments need to be converted.

print(type(str(5)))
print(int(45.89))
x = float(23)
print(type(x), x)
y = complex(45)
print(y)
z = bool(-2)  #NOTE : expext 0, everything results as True 
print(z)