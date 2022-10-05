#Arithmetic operators
#Comparison operators
#Assignment Operators
#Logical Operators
#Bitwise Operators
#Membership Operators
#Identity Operators

#Arithmetic operators
        #order of precedence:  (), ** ,*,/,//,%,+,-

print(2**3)                 #exponentail
print(2*3)                  #subtraction
print(2/5)                  #division
print(5//2)                 #integer/floor devision
print(8%2)                  #modulus
print(4+5)                  #addition
print("hello"+"python")     #addition of string
print(3-5)                  #subtraction
print((5%6+3/4) - (45*0-2))

#Comparison Operators
    #comparison operator is usually used to compare 2 values
    #resultant is always a boolean value
    # 

print(2==2)                 #if booth are equal
print(2!=2)                 #if not equal(! is used as not)
print(2<3)                  #less than 3
print(2>3)                  #greter than 3
print(2<=3)                 #less than equal
print(2>=3)                 #greater than or equal

#Assignment Operators
    #The assignment operators are used to assign the value of the right expression to the left operand
assignmentOperator = "hi, there"        #assigns the value of the right expression to the left operand
aNum1 = 20                              
aNum1+=20                               #this operators means aNum = aNum + 20. i.e : aNum = 20+20, which is equal to 40.
aNum1-=20                               #vise versa operations with subtration
aNum1*=7
aNum1/=2
aNum1 %= 7
aNum1 **= 2
aNum1 //=1
print(aNum1)

#Logical Opearators
    #and,or, not
    #here again the resultant is a boolean value
    #and : if both are true, then the output is true
    #or : if any one is true, then the output is true
    #not : it reverse the expression value for the opposite boolean value
    #usually used in if cluase

print((8>3) and (6>4))
print((3>1) or (4<=1))
print(not(4==2))

#bitwise operator
# &, |, ~, >>, << 
a = 60            # 60 = 0011 1100 
b = 13            # 13 = 0000 1101 
c = 0

c = a & b;        
print(c) 

c = a | b;        # 61 = 0011 1101 
print( c)

c = ~a
print(c)          #a = -61


#Membership Operators
    #in, not in
    #used to check whether the elements are present are in the given data type
lst = ['a','b', 'c']
print('a' in "hello a")
print("c" not in lst)
print("a" in lst)


#Identity Operators
    #is, is not 
    #The identity operators are used to decide whether an element certain class or type.
    #is and == are different
x1 = [2,3,4,5,6,7,8]
y1 = [2,3,4,5,6,7,8]
z = x1

print(x1 is z)
print(x1 is not y1)