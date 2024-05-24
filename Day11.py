#string 
names = "snehal"
lastname = 'kamble'

father = """kawadu"""
mother = '''jyotsna'''


##we cam write string in ''," ",""" """,''' '''


## string stores the value by index


# name = "snehal"
# print(name)


# print(name[2])
# print(name[0])



# string does not support item assignment
# check for sub-string or particular char


names="jyotsna"
print(names)

# "j" in names

# print(names)



name="snehal"
print("s" in name)
print("S" in name)
print("al" in name)

for i in range(4):
    print(i)



#range
for x in range(len(name)):
    print(x)      

##witout range
for x in name:
    print(x)


##while
i = 0
while(i<len(name)):
    print(i)
    i= i+1


##length

name="nikita"
print(name)
print(len(names))  ##7


##upper()
q1=name.upper()
print(q1)

##lower()

names2="POOJA"
q2= names2.lower()
print(q2) 



 ##capitilize()


q3=name.capitalize()
print(q3)  ## only captilize the first letter in string 


q4=name.startswith("n")
print(q4)

##stratwith

##startwith also work wit substrings -- true or false


q5 = name.startswith("niki")
print(q5)


##replace
name3 ="samikshaa and snehal are sister"
q6=name3.replace("sister","friends")
print(q6)

##endwith  -- true false

q7=name.endswith('ta')
print(q7)


##join()
name4="samiksha,sakshi","sayli"
q8='$'.join(name4)
print(q8)




##isupper()

names="SNEHAL"
q1=names.isupper()
print(q1)


###islower()
q2=names.islower()
print(q2)


info="snehal"
q3=info.islower()
print(q3)


num="155454545"
q4=num.isdigit()
print(q4)


A='jvshxuasvxuasc'
a2=A.isalpha()
print(a2)



ex="csc455544"
a3=ex.isalnum()
print(a3)


ex="csc4555**((44"
a5=ex.isalnum()
print(a5)


##join

info1=["snehal","kamble"]
q1="@".join(info1)
print(q1)


##strip

ex="  mumbai "
q2=ex.strip()
print(q2)
print(len(ex))


###lstrip

q3=ex.lstrip()
print(q3)


##rstrip
q4=ex.rstrip()
print(q4)


name="snehal"   
a4=name.index("s")
print(a4)

a2=name.index("ha")
print(a2)




# ##split
# city="Hinganghat"
# q5=city.split[city[4:9]]
# print(q5)
