##set 
#3set does not allow duplicate value
 ##set does not store value by index
##list store value by index 


setA={1,5,22,4,65,35,98,22} ##does not allow duploacte value

print(setA)



names=["snehal","chinmay","sayli","mani","sami","snehal"]
print(names) ##store dupliactes values

print(names[0])

## collections  --> list , string , tuple , dictionary ,set

a ="snehal" ## string 
b=('snehal',"samiksha") ##tuple
c ={"name":"snehal"} ##dict 
d =[1,5,42,3] ##list
e={"sneha","mani"} ##set  {1,2,4,7,6,} -- set 

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

A =[14,55,99]
B=[45,88,78]
print(max(A))
print(len(B))
print(min(A))
print(len(A))


A={47,11,44,55,84,45,22,55,88,65}
A.add(44)
print(A)

B=A
B.add(75)
print(B)

A.pop()
print(A) #delete random num

A.remove(44)
print(A)


B=A.copy()
B.remove(47)
print(A)
print(B)

setA={'snehal','chinmay','sayli'}
setB={'mani','ajay','sakshi'}
setB=setA.copy()
setA.pop()
print(setA)
print(setB)

##union method

set1={14,55,78,96,33,79}
set2={47,55,33,78,22,2,88}
set3= set1.union(set2)
print(set3) ##{96, 33, 2, 14, 78, 47, 22, 55, 88}


set4=set1.intersection(set2)
print(set4) ##{33, 78, 55} --return common items


set2.intersection_update(set1)
print(set2)

set5 = set1.difference(set2)
print(set5) ##{96, 14,79} --uncommon item 

set2.difference_update(set1)
print(set2) ## {2, 22, 88, 47} 


set1.difference_update(set2)
print(set1) ##{96, 33, 55, 14, 78,79}


set1={14,55,78,96,33,79}
set2={47,55,33,78,22,2,88}

seta=set2.symmetric_difference(set1)
print(set1) ##{96, 33, 55, 14, 78,  79}

q1=set1.issubset(set2)
print(q1) ## false

q2=set1.issuperset(set2)
print(q2) ## false

a=set1.isdisjoint(set2)
print(a) 




















