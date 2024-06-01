##tuple

##method in tuple

#list is mutable data type

# fruits=["banana","apple","kiwi","manago"]
# print(fruits)
# print(type(fruits)) ##--- list  



##tuple is a inmutable degta type 


fruits2=("banana","apple","kiwi","grapes")
print(fruits2)
print(type(fruits2))  ## -- tuple



tup_num=(12,54,85)
print(tup_num)
print(type(tup_num)) ## -- tuple 


tup_number=(8)
print(tup_number)
print(type(tup_number))  ## -- int becuse single value 




tup_number=(8,)  # tuple with a single element
print(tup_number)      ##--- tuple beacuse of , its makes tuple 
print(type(tup_number))


##tuple have only 2 methods index and count 




fruits=("banana","apple","kiwi","manago")
print(fruits.count("banana"))

# count , no of times the item has appeared
###--------------------------------------------------------



###index

print(fruits.index("kiwi"))  ## index return postion in index 


##---------------------------------------------



# packing and unpacking of tuple
fruits = ('apple','kiwi','banana') #packing of tuple
print(fruits[0])
print(fruits[1])
print(fruits[2])


for i in fruits:
  print(i)


  a , b ,c = fruits #unpacking of tuple

print(a)
print(b)
print(c)


a, b ,x = fruits #unpacking of tuple

print(x)

_,k,_ =  fruits #unpacking of tuple

print(_) # as a placeholder
  


