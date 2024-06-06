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
e={"sneha","mani"} ##set 

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





del setB





