names=["snehal","sarika","nikita","shreya","lalita"]
print(names)

print(names[0])

number=[21,55,41,23,14,33]
print(number)

number[0]=222 
print(number)

names2=["chinmay","snehal","vedant","sayli"]
print(names2)

names2[2]="saru"
print(names2)

names3 = names2.copy()
print(names3)
print(names2)
names3[0]="samir"
print(names3)



dict = {
    "firstName":"snehal",
    "lastName":"kamble"
}

dict2 = dict 
dict2['firstName'] = "nikita"
print(dict2)
print(dict)

dict3 = dict.copy()
dict3['firstName'] = "samir"
print(dict3)
print(dict)


names = ["chinmay","snehal","rahul"]

def addElement(lst):
    #lst = names
    lst.append("niki")
    return lst 
a = addElement(names)
print(a)
print(names)

