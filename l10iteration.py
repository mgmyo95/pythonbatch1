# => for in loop 
# Iteration a list 


colors = ["red","green","blue"]

for color in colors: 
    print(color)

# Iteration in string 
message = "Hello World"
print(len(message))  # 11 

for msg in message:
    print(msg)


# Iteration a dictionary 
students = {"name":"su su","age":20,"city":"Mandalay"}
print(students)
print(students.items()) # dict_items([('name', 'su su'), ('age', 20), ('city', 'Mandalay')])

for key in students:
    print(key,students[key])

for key,value in students.items():
    print(key,"=",value)


# => range() in for in loop 
for x in range(10):
    print(x) # 0 to 9 

print(f"Outside x value is {x}") # Outside x value is 9



for y in range(1,5):
    print(y) # 1 to 4 

print(f"Outside x value is {y}") # Outside x value is 4


for p in range(1,10,2):
    print(p) # 1 3 5 7 9 

print(f"Outside x value is {p}") # Outside x value is 9

# => break and continue

for i in range(10):
    if i == 5:
        break # skip even number 5
    print(i)

print(f"Outside i value is {i}") # Outside x value is 9


for j in range(10):
    if j % 2 == 0:
        continue # skip even numbers 
    print(j)     # 1 3 5 7 9

print(f"Outside i value is {j}") # Outside x value is 9


# Nested Loops 

staffs = [
    ["aung aung","kyaw kyaw","zaw zaw"],
    ["su su","nu nu","yu yu"],
    ["thidar","nilar","muyar"]
]

# for staff in staffs:
#     for people in staff:
#         print(people)
   

# for staff in staffs:
#     for people in staff:
#         print(people,end=" ")



for staff in staffs:
    for people in staff:
        print(people,end=" ")
    print()


# => while loop 

idx = 0 

while idx < 10:
    print(f"Index : {idx}")
    idx += 1

print(f"Outside idx value is {idx}") # Outside idx value is 10 


count = 0 

while count < 10:
    count += 1
    print(f"Index : {count}") # 1 to 10 
    

print(f"Outside idx value is {count}") # Outside idx value is 10 


paints = ["red","green","blue"]
print(paints) # "red","green","blue"] 
print(enumerate(paints)) # <enumerate object at 0x756216519e40>


for index,paint in enumerate(paints):
    print(index,paint)


index = 0 
while index < len(paints):
    print(index,paints[index])
    index += 1 


# 10IT 
