if True:
    print("Yes")
else:
    print("No")

if False:
    print("Yes")
else:
    print("No")

if 5 == 5:
    print("Yes")
else:
    print("No")

if 1 >= 1:
    print("Yes")
else:
    print("No")


if 3 <= 3:
    print("Yes")
else:
    print("No")


a = [10,20,30]
b = a 
c = [100,200,300] 

print(a is b) 
print(b is a)
print(a is not c)


x = [10,20,30,40,50]
print(30 in x)
print(499 in x)
print(500 not in x)

print("e" in "orange")
print("o" not in "orange")


girls = ['su su','yu yu','nu nu']
print('yu yu' in girls)
print('Yu Yu' in girls)
print('yu' in girls)

if isinstance("Hello",str):
    print("Yes")
else:
    print("No")

if isinstance(300,int):
    print("Yes")
else:
    print("No")

if isinstance(3.33,float):
    print("Yes")
else:
    print("No")

if isinstance(False,bool):
    print("Yes")
else: 
    print("No")

if isinstance(['aye aye'],list):
    print("Yes")
else:
    print("No")

if isinstance({"name","aung aung"},dict):
    print("Yes")
else:
    print("No")