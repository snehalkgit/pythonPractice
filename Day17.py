#program 1 


names=["snehal","chinmay",'sayli','vrushali',"sanket"]
print(names) ## list


cities=("mumbai","pune","goa","nagpur")
print(cities)
print(type(cities)) ## tuple 



##program 2

print(cities[0])
print(cities[2])

##program 3 

cities=("mumbai","pune","goa","nagpur")
##loop

for x in range (len(cities)):
 print(x)
print(cities[x])


for x in cities:
    print(x)   


##while
i = 0
while(i< len(cities)):
   print(i)
   print(cities[i])
   i = i + 1



names=("snehal","chinmay",'sayli','vrushali',"sanke","samiskha")   

print(names)
print(type(names))

names=("snehal","chinmay",'sayli','vrushali',"sanke")   
#unpacking 

a,b,c,d,e= names
print(b)
print(a)
print(c)



##program 4 

city=["pune","munbai","hinganghat"]
def addcity(lst):
   lst.append("goa")
   return tuple(lst)

w,x,y,z = addcity(city)
print(w)
print(x)


s=(47,55,86,98,52,36)
s=list(s)
s.append(44)
s = tuple(s)
print(s)

k = s.count(22)
print(k)
a= s.index(55)
print(a)







