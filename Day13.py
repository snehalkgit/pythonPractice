##methods
name=["snehal","kamble",24,8]
print(name)
print(name[1])
## retrive

print(name[0])

##update

name[0]="nikita"
print(name)


##add

#name.append('city')
print(name)

##delete

name.pop()
name.remove("nikita")
print(name)

##if available

print("kamble" in name)




##dictionary----------
# dictionary does not stores the value by index and write in double cotted 

##dict

name2={
    "firstname":"snehal",
    "lastname":"kamble",
    "age":24,
    "seatno":22

}

##retive

q1 = (name2['firstname'])
print(q1)

q2 = name2['lastname']
print(q2)

##update

q3 = name2['age']=25
print(q3)


name2["seatno"]=55
print(name2)


##add

name2['city']="mumbai" ##if not present so it will add new 
print(name2)


name2['color'] = "black"
print(name2)  ##if present soo it will update 


##delete 

name2.pop('age')


# del name2
# print(name2)



##program2 

bank={
    "branchname":"maharashatra bank",
    "holdername":"snehal kamble",
    "regno":12545655555

}
##retrive 

print(bank)
print(bank["branchname"])
print(bank["regno"])


##update

bank["branchname"]="sbi"
print(bank)


bank["city"]="hinganghat"
print(bank)



##add

bank['age'] = 24
print(bank)


#delete 

bank.pop('age')
print(bank)


a=len(bank)
print(a)


print("city"in bank)
print("snehal kamble" in bank) ## reteun false value 
print('maharashatra bank' in bank) ## false



## *** Keys are the Primary Index **** 





