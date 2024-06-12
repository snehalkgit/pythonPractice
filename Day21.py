##lambda function
  ## program 1


def add(a,b):
    return  a+b
c = add(14,5)
print(c)


##program 2

add = lambda a,b:a+b
s=add(41,8)
print(s)

##program 3 

sub = lambda x , y : x - y
s1=sub(14,5)
print(s1)

mul = lambda x  : x * 5
s1=mul(7)
print(s1)


squ= lambda y : y* y
s2=squ(22)
print(s2)


div = lambda x : x / 5
d=div(14)
print(d)


##program 4

##function as paramter ato another function


add = lambda x,y:x +y
def addi (fn,x,y):
    e=(fn,x,y)
    return e 
s= add(14,55)
print(s)


sub = lambda a , b : a - b
def subt (fn,a,b):
 s= (fn , a, b)
s=sub(14,2)
print(s)



##function as a paramter to another function

def subt( fn,u,v):
   fn = lambda u,v:u-v
   return fn(u,v)
a=sub(15,8) ## (lambda u,v:u-v,15,8)
print(a)



##function as a  return type

def mult():
   return lambda  x : x * x
c = mul(5)
print(c)


##program 5 

##default 


def add(a=41,b=8): ##default value set 
   print(a+b)

add(41,50)
add()



##postional arguments 

def subt(a,b):
   return a - b 
a = sub(47,2) ## 45 
print(a)
b = sub(a=87,b =66) ## 21
print(b)


##args


def add(*a):
   print(a)
   total = 0
   for i in a:
      total = total + i 
   return total 
ans= add(1,4,5,6,8,5,6,88,21,45,32,14,5,96,75,22)
print(ans)


#args 
def add(*agrs):
    print(agrs)
    total = 0
    for i in agrs:
        total = total + i
    return total
t = add(234,5,6,3,4,5,5,6,7,3,5,6,7,4,6,7,6,7,8)
print(t)


##kwargs -- varible
def sub(**b):
   print(b)
   b['language']="English"
   return b 
s=sub(name="snehal",age="25")
print(s)


def sub(**b):
   print(b)
   return b 
s=sub(15,5,8,7,41,25,63,58,69)
print(s)
























