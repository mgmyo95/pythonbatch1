#! Function (6) def = define 
#? 1. Simple Function with No Parameters 
#? 2. Function with Parameter 
#?         (i) Single Parameter Function
#?         (ii) Multi Parameter Function 
#? 3. Function with Default Parameter
#? 4. Function with a Return Value 
#? 5. Function with multi Return Value 
#? 6. Lambda Function (Anonymous Function)


#? 1. Simple Function with No Parameters 
def sayname():
    print("Hello Aung Aung")  # execute 

sayname() # invoke die
sayname()



#? 2. Function with Parameter 
#?         (i) Single Parameter Function

def saycity(city):
    print("hello " + city)

saycity("Mandalay")
saycity("Yangon")


#? 3. Function with Default Parameter
def country(country="Thailand"):
    print(f"Hello {country}")

country()
country("Myanmar")
country("Indonesia")


#? 4. Function with a Return Value 

def sayage():
    return ("I am 28 years old")

print(sayage())


#? 5. Function with multi Return Value 

def saynickname():
    result = "Daw Pu"
    return result

print(saynickname())


def saynum(num1=20):
    return num1 

print(saynum(100))
print(saynum())

# f = keyword
def greeting(value="yamin"):
    return f"Hello {value}"

print(greeting("Su Su"))
print(greeting())


def funone(num1,num2):
    result = num1 + num2 
    return result 

print(funone(10,20))

def funtwo(num1,num2=200):
    result = num1 + num2 
    return f"Total value is = {result}" 

print(funtwo(10))
print(funtwo(10,20))



#? 5. Function with multi Return Value 

def saynameandage():
    name = "Honey"
    age = 26 
    city = "Yangon"
    return name,age,city

print(saynameandage()) # ('Honey', 26)


name,age,city = saynameandage() 
print(name) # Honey
print(age) # 26 
print(city) # Yangon


#? 6. Lambda Function (Anonymous Function) 

addresult = lambda num1,num2,num3:num1+num2+num3 
print(addresult(200,300,400))


sumresult = lambda num1,num2=200,num3=500:num1+num2+num3 
print(sumresult(200,300,400))
print(sumresult(200,300))
print(sumresult(100))   



# inputval = input("Enter your name = ")
# msg = "Hello " + inputval
# msg = "Hello %s" % inputval # version 2
# msg = f"Hello {inputval}" # version 3 
# print(msg)


firstname = input("Enter First Name = ")
lastname = input("Enter Last Name = ")
# fullname = "Hello %s%s" % (firstname,lastname) # version 2
# fullname = "Hello %s %s" % (firstname,lastname) # version 2 
fullname = f"Hello {firstname} {lastname}" # version 3
print(fullname)

# 6IT






