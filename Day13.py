##dictionary and   methods in dict


info={
    "name" : "snehal",
    "age":24,
    "area":"hinganghat",
    "skills":['js','sql','python',['typescript','cypress','c++']]

}

# get() to access the values


print(info.get('name'))
print(info.get("age"))
print(info.get('area'))

print(info.get('skills')[2])
print(info.get('skills')[3][2])


###
# keys() will get all the keys from the dictionary
# values()
# items()


print(info.keys())
print(type(info))
print(info.values())
print(info.items())


for s in info.values():
    print(s)
 ## values 



for s in info.keys():
    print(s) ## keys




for s in info.items():
    print(s)     ## items  gives keys and their values



#  dictionary : indexing ? are dictionary ordered : YES
# Dictionary is a mutable data type
# Dictionary is ordered 


##-----------------------------------------------------------

info2={


    'samir':45,
    'snehal':88,
    'kajal':90,
    'mani':60
}

# updating a dictionary
# update({key:value})


info2.update({'snehal':99})
print(info2)


info2.update({'mani':75})
print(info2)



# setdefault()
# setdefault() = get() + update()

# working as get()

print(info2.get("snehal"))
#print(info2.setdefault("nikita"))
print(info2.setdefault("nikita",99))
print(info2)

# if the key does not exist , key will be addded by the setdefault method with value as 'None'

# using get() we can inform the user about key 

##--------------------------------------------------------------------------------------
##removing items


info3={
    "name" : "snehal",
    "age":24,
    "area":"hinganghat",
    "skills":['js','sql','python',['typescript','cypress','c++']],
    "hobby":({"dancing","redaing"})

}
print(info3)

print(info3.pop('age'))


# will remove the last added item
# popitem()

print(info3.popitem())
print(info3)



# Initialising a dictionary
# fromkeys('keys',value)


students_list=["snehal","nikita","saru","chinmay"]
print(students_list)


print(dict.fromkeys(students_list))
print(dict.fromkeys(students_list,85))
print(dict.fromkeys(students_list,88))
print(dict.fromkeys(students_list),55)
print(students_list)


list_val = [18,200,300]

print(dict.fromkeys(list_val,"NA"))



list_fruits = ['apple','banana' , 'kiwi']

print(dict.fromkeys(list_fruits,"In Stock"))
print(dict.fromkeys(list_fruits,"not in stock"))
print(dict.fromkeys(list_fruits,"avaliable"))
