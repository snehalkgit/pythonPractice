##program 1


names =["snehal","chinmay","sarika","sayli","sushnt","pratik"]
print(names)
print(names[0])
print(names[5])

##program 2 

##curd opertaion === retrive update delete addd

##value retrive
print(names)

##add value

print(names.append("vrushali"))
print(names)

print(names.append("soonu"))
print(names)


##value update

names[1]="monika"
print(names)

names[5]="sam"
print(names)



##delete value  === pop


names.pop()
print(names) ## delete last elemenets

names.pop(2)
print(names) ##delete specifc element 



##program 4 

fruits=["banana","apple","mango","kiwi"]
print(fruits)



fruits.append("chiku")
print(fruits)

## in 

print("banana" in fruits)
print("kiwwi" in fruits)


if("banana" in fruits):
    print("present")
else:
    print("absent")   


  ##program 5

city = ["mumbai","pune","nagpur","hinganghat"]
print(city)

##for -- range 

for x in range(4):
    print(x)
    print(city[x])



for x in range(len(city)):
    print(city[x])


    ##without range

    for ci in city:
        print(ci)
        print(ci[0])


for c in city:
    print(c)


for x in range(len(city)):
    print(city[x])


    










