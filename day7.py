# methods 
names = ["snehal","purva","chinmay","sayli","rahul"]
print(names)
names2 = names
names2[0] = "nikita"
print(names2)
print(names)

# program 2
cities = ["wardha","pune","mumbai","kolkata"]
citiesB = cities.copy()
citiesB[0] = "nagpur"
print(cities)
print(citiesB)

# program3 

country = ["india","srilanka","china","pakistan","dubai"]
country.pop()
country.pop(2)
##country.remove("china")
print(country)
print(country)

# program 4
numbers = [11,22,33,44,55,6,85]
numbers.append(254)
print(numbers)

numbers.insert(3,259)
print(numbers)



marks1 = [55,54,125,45,23,66]
marks1.extend([81,55,36,95,75,14,52,23])
print(marks1)


# program 5
#          
fruits = ["apple","mango","grapes","papaya","apple" , "kiwi","coconut"]
y = fruits.count("apple")
print(y)
g = fruits.index("kiwi")
print(g)


fruits.reverse()
print(fruits)

fruits.sort()
print(fruits)
