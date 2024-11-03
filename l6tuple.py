# List Vs Tuple 
# 1. Mutablity . mutable (changeable) and immutable (not changeable)
# 2. Performance 
    #  list : Generally slower than tupples 
    # tuple : Faster and more-efficient . Because they are immutable and have a fixed size 
# 3. Use Cases 
    # list: need to change , use lists , shooping carts , etc...
    # tuple : geographic coordinates , settings , database records 
# 4 . Methods 
    # list : many built-in methods for modifying list. .append(),.remove(),.pop(),.sort()
    # tuple : fewer built-in methods, cannot be modified,  only can use .count(),.index()

print(type([1,2,3])) # <class 'list'>
print(type((1,2,3))) # <class 'tuple'>

# Create a tuple with parentheses 
tuple1 = (1,2,3,4,5) 
print(tuple1) # (1, 2, 3, 4, 5)



# Create a tuple without parentheses 
tuple2 = 10,20,30,40,50,20 # (1, 2, 3, 4, 5)

 
print(tuple2)

print(tuple2[0]) # 1
print(tuple2[2]) # 3 

print(tuple2[3]) # 40
print(tuple2[4]) # 50

# tuple1[0] = 100 # TypeError: 'tuple' object does not support item assignment
# tuple2[0] = 100 # TypeError: 'tuple' object does not support item assignment


print(tuple1.count(1)) # 1 
print(tuple1.count(10)) # 0 

print(tuple1.count(20)) # 2
print(tuple1.count(200)) # 0 

print(tuple1.index(4)) # 3

print(tuple2.index(20)) # 1 
print(tuple2.index(50)) # 4

# Tuple Unpacking 
students = ("aung aung","su su")

boy,girl = students 
print(boy) # aung aung
print(girl) # su su

# Nested Tuples 
numbers = (1,(2,3),(4,5,6))
print(numbers)   # (1,(2,3),(4,5,6))
print(numbers[1]) # (2, 3)

print(numbers[2][3]) 
