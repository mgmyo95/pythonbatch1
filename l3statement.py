if True:
    print("Yes") 
else:
    print("No")


if False: 
    print("Yes")
else: 
    print("No")


if 5 == 5:      # must be one space 5 == 5
    print('Yes')
else: 
    print("No")

if 5 != 3:      # must be one space 5 == 5
    print('Yes')
else: 
    print("No")

if 5 > 1:
    print("Yes")
else:
    print("No")

if 5 >= 5:
    print("Yes")
else:
    print("No")

if 5 < 1:
    print("Yes")
else:
    print("No")

if 5 <= 5:
    print("Yes")
else:
    print("No")


a = [10,20,30]
b = a 
c = [1000,2000,3000]

print(a is b)  # True 
print(a is c)  # False 
print(a is not c)  # True


x = [10,20,30,40,50]
print(20 in x)      # True 
print(5 in x)      # False 

print("e" in "student")      # True 
print("o" not in "orange")      # False 

girls = ['su su','yu yu','nu nu']
print('yu yu' in girls)     # True 
print('Yu Yu' in girls)     # False 
print('yu' in girls)        # False



# => isinstance(val,type) hoke tl lr / function 

if isinstance('Hello',str):
    print('Yes')
else: 
    print("No")


if isinstance(5,int):
    print('Yes')
else: 
    print("No")


if isinstance(5.67,float):
    print('Yes')
else: 
    print("No")


if isinstance(False,bool):
    print('Yes')
else: 
    print("No")


if isinstance(['su su'],list):
    print('Yes')
else: 
    print("No")


if isinstance({"name":"nu nu"},dict):
    print('Yes')
else: 
    print("No")








#Comparison Operator 
# == Equal 
# != Not Equal 
# > Greater Than 
# < Less Than  
# >= Greater Than or Equal To 
# <= Less Than or Equal To 
# is, is not      Identity Operators 
# in , not in     Membership Operator 





#! Function (6) def = define 
#? 1. Simple Function with No Parameters 
#? 2. Function with Parameter 
#?         (i) Single Parameter Function
#?         (ii) Multi Parameter Function 
#? 3. Function with Default Parameter
#? 4. Function with a Return Value 
#? 5. Function with multi Return Value 
#? 6. Lambda Function (Anonymous Function)



def sayname():
    print("Hello Aung Aung")  # execute 

sayname() # invoke die
sayname()

# 29FN



# name() simple function
# name(val)  parameter function , regular function
# name(val1,val2)
