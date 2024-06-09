##function

##program 

##int 

def add(x,y):
    return x + y
a=add(4,9)
print(a)


def sub(x,y):
    return x-y

b=sub(50,5)
print(b)


####float

##float as a parameter and float as return type

def add(x,y):
    return x+y
c=add(14,7)
print(c)


def add(x,y):
    return x+y
d=add(14.7,32.2)
print(d)


##string

##string as a parameter and string as a rrturn type

def greet(name):
    return "hiii" +name
e=greet("snehal")
print(e)


##bollean 

##bollean as a parameter and bollean as a return type

def candrive(above18):
    if above18:
        return True
    else:
        False
f=candrive(False)
if(f):
    print('allow to drive')
else:
    print("not allowed")     




def candrive(above18):
    if above18:
        return True
    else:
        False
f=candrive(True)
if(f):
    print('allow to drive')
else:
    print("not allowed")     


##list 
##list as a parameter and list as a return type

name =["snehal","sayli","chinmay","sami"]
def addname(listA):
    listA.append("mani")
    return listA
s=addname(name)
print(s)



##dictn

##dict as a parameter and dict as  a return type

dicta={
    "fn":"sneha",
    "ln":"kamble"
}

def addcitytodict(name):
    name['city']="mumbai"
    return name
a=addcitytodict(dicta)
print(a)


##tuple

##tuple as a parameter and tuple is return type

tupA=()
def addno(tupA):
    tupA=list(tupA)
    tupA.append(45)
    tupA = tuple(tupA)
    return tupA
k=addno((4,5))
print(k)


##set

##set as a parameter and set as a return type

setA={48,55,76,8}
def addno(k):
    k.add(2)
    return k

a=addno(setA)
print(a)


    