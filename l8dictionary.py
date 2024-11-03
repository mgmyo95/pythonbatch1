student = {
    "name" : "Su Su",
    "age" : 20,
    "city" : "Yangon"
}

print(student) # {'name': 'Su Su', 'age': 20, 'city': 'Yangon'}
print(student["name"]) # Su Su
print(student["age"]) # 20
print(student.get('city')) # Yangon


# Method 2 dict()
staff = dict(name="Aung Aung",age=30,city="Mandalay")

print(staff) # {'name': 'Aung Aung', 'age': 30, 'city': 'Mandalay'}
print(staff["age"])
print(staff.get('city'))

# print(student["country"]) # keyError 
# print(staff["country"]) # keyError 

print(student.get("country")) # None
print(staff.get('country')) # None

print(student.get('country','Myanmar')) # Myanmar
print(staff.get('country','Thailand')) # Thailand
 
print(student.get("age",40)) # 20
print(staff.get("age",50)) # 30


employee = {
    "name" : "aung aung",
    "age" : 30,
    "city" : "Mandalay"
}
 
print(employee) # {'name': 'aung aung', 'age': 30, 'city': 'Mandalay'}

employee['email'] = "aungaung@gmail.com"
print(employee) # {'name': 'aung aung', 'age': 30, 'city': 'Mandalay', 'email': 'aungaung@gmail.com'}

employee["age"] = 25
print(employee)  # {'name': 'aung aung', 'age': 25, 'city': 'Mandalay', 'email': 'aungaung@gmail.com'}

del employee["city"]
print(employee) # {'name': 'aung aung', 'age': 25, 'email': 'aungaung@gmail.com'}






worker = dict(name="Nilar",age=18,city="Bago")
 
print(worker) # {'name': 'aung aung', 'age': 30, 'city': 'Mandalay'}

worker['email'] = "nilar@gmail.com"
print(worker) # {'name': 'Nilar', 'age': 18, 'city': 'Bago', 'email': 'nilar@gmail.com'}

worker["age"] = 25
print(worker) # {'name': 'Nilar', 'age': 25, 'city': 'Bago', 'email': 'nilar@gmail.com'}

del worker["city"] 
print(worker) # {'name': 'Nilar', 'age': 25, 'email': 'nilar@gmail.com'}





