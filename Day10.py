##list 

##program 1 

names=["snehal","chinmay","sarika","sayli","pratik","mani"]
print(names)
print(names[2])
print(names[1])
names.append("nikita")
print(names)

## string 

first_name = "snehal"
print(first_name)
print(type(first_name))   ## class string 


##string store the value by index


names2=["snehal","sarika","manisha","sonu","dipti"]
print(names2)
print(names2[2])



##we cannot update cahr of sting

nameA = "snehal"
print(nameA)

for x in range(len(nameA)):
    print(x)
    print(nameA[x])



for name in nameA:
    print(name)


i1 = 1
while (i1 <len(nameA)):
    print(i1)
    print(nameA[i1])
    i1 = i1+1


##slice


city = "Hinagnghat"
print(city)

print(city[1:5])
print(city[1:9:1])
print(city[-5:-2:2])
print(city[::1])
print(city[-9:-1:1])
print(city[1:10:])

print(city[2:-2])


   