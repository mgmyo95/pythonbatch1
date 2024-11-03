name = "aung kyaw"
print(name)
print(name[0]) #a
print(name[3]) #g
print(name[8]) #w 
print(name[-1]) #w
print(name[-2]) #a
print(name[-6]) #u 

#start:end:step 
print(name[0:1]) #a 
print(name[0:2]) #au
print(name[0:3]) #aun
print(name[0:4]) #aung


print(name[1:4]) #ung 
print(name[1:7]) #ung ky
print(name[0:9]) #aung kyaw

print(name[0:9:1]) #aung kyaw
print(name[0:9:2]) #an yw
print(name[0:9:3]) #agy


fullname = name  # aung kyaw
fullname = name[:]  #aung kyaw
fullname = name[0:4] #aung
fullname = name[::-1] #wayk gnua
print(fullname) # aung kyaw 

getlength = len(name)
print(getlength) #9 

text = "hello friend"
print(text.upper()) # HELLO FRIEND 

print(text.capitalize()) # Hello friend
print(text.title()) # Hello Friend 

task = "HAVE TO GO"
print(task.lower()) # hello friend 
print(task.casefold()) # hello friend 


todo = "Have to Shop"
print(todo.swapcase()) #hAVE TO sHOP 

hifi = "    hello friend    "
print(hifi) #    hello friend 
print(hifi.strip()) #hello friend 
print(hifi.lstrip()) #hello friend
print(hifi.rstrip()) #  hello friend


greet = 'hello friend'
print(greet.replace('friend','sir')) #hello sir 
print(greet.replace("Friend",'sir')) #hello friend

print(greet.startswith('h')) # True 
print(greet.startswith("he")) # True
print(greet.startswith("H")) # False 
print(greet.startswith("He")) # False 

print(greet.endswith("nd")) # True
print(greet.endswith("frined")) # False 
print(greet.endswith("Friend")) # False


mobile = "OPPO"
print(mobile.isupper()) # True 
print(mobile.islower()) # False


num1 = 528 
num2 = "1500"
num3 = "ten" 
num4 = "number ten"
num5 = "hay!"

# print(num1.isdigit()) # error cuz of isdigit() can check only for string 

print(str(num1).isdigit()) # True 
print(num2.isdigit()) #True
print(num3.isdigit()) #False

print(num2.isalpha()) # False
print(num3.isalpha()) # True

print(num2.isnumeric()) # True
print(num3.isnumeric()) # False

print(num2.isalnum()) # True
print(num3.isalnum()) # True

print(num4.isalnum())  # False (cuz of sapce)
print(num5.isalnum()) # False (cuz of !)


middlename = " "
print(middlename.isspace()) # True 

nickname = "Aung Moe"
print(nickname.isspace()) # False 別の単語があるから　だめ
print(nickname.istitle()) # True

sayhi = "Hi My Friend" 
print(sayhi.split()) # ['Hi', 'My', 'Friend'] 

color = "red,green,blue,white,black"
print(color.rsplit()) # ['red,green,blue,white,black'] 

sayhello = "Hello\nFriend\nAung" # \n new line 
print(sayhello.splitlines()) # ['Hello', 'Friend', 'Aung'] 


sayhifi = "Hello Friend Mr.Maung"
print(sayhifi.partition(" ")) # ('Hello', ' ', 'Friend Mr.Maung') 
print(sayhifi.partition(".")) #  ('Hello Friend Mr', '.', 'Maung')

post = "Read"
print(post.ljust(10,'-')) # Read------ susupaung lenght ka 10 lon shi ya ml 
print(post.rjust(10,'-')) # ------Read 
print(post.center(10,'-')) #---Read---


city = "Hello {}"
print(city.format("Mandalay")) # Hello Mandalay 

country = "Hello {} {}"
print(country.format("Mandalay","Myanmar")) # Hello Mandalay Myanmar

print("Hello my {}.are you {}!".format("Friend","Aung Aung")); #Hello my Friend.are you Aung Aung!

val1 = "sister"
val2 = "Su Su"
print("Hello my {}.are you {}!".format(val1,val2)) # Hello my sister.are you Su SU!


# dictionary 
student = {"name":"Su Su"}
sayname = "Dear , {name}"
print(sayname.format_map(student)) # Dear , Su Su 

# 13SM


message = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."

countoflorem = message.count("Lorem")
print(countoflorem)  # 1

countofdolor = message.count("dolor")
print(countofdolor) # 4

