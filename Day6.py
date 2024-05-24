##list

names=["snehal","sayli","prtik","chinmay","mayur","subhu"]
print(names)

print(type(names))

##retrive

print(names)

##add

print(names.append("sarika"))
print(names)

##update

names[0]="sush"
print(names)


#delete

names.pop()
names.pop(2)
print(names)


##-------------------------------------------------------------------

cities=["mumbai","pune","hinganghat","wardha","kolkata"]
print(cities)
print(cities[2])

print("mumbai" in cities)
print("goa" in cities)


##loop
for x in range(len(cities)):  ### with range
  print(x)
  print(cities[x])


for citi in cities:
  print(citi)   ## without range 




##while 
i1 = 0
while i1< len(cities):
  print(cities[i1])
  i1= i1+1


i2= 0
while i2<(5):
  print(cities[i2])
  i2=i2+1


fruits=["mango","apple","pineapple","chikoo","orange","kiwi"]
print(fruits)
print(fruits.append("bananana"))
print(fruits)


print(fruits.pop())
print(fruits)



##remove

print(fruits.remove("kiwi"))
print(fruits)



##clear == will be empty data delete

# print(fruits.clear())
# print(fruits)


##list will be empty


number=[1,22,55,22,66,44,]
number1=[45,88,25,2,36]

number.insert(1,25)
print(number)

number1.insert(2,23)
print(number1)



#extend
x = [1,2,3,4,5,6]

y = [4,5,22,52,5,6,]

x.extend(y)
print(x)


y.extend(x)
# print(y)


# print(x)
# print(y)




