
##program 1
birthyear=[1998,1997,1996,1980,1989]

currentage = []
for x in birthyear:
 print(x)
 print(2024-x)
 age = 2024 - x
 currentage.append(age)
 print(currentage)


 ##program 2
 marks=[21,60,69,55,88,55,88]
 above50=[]
 for x in marks:
  print(x)

for x in marks:
 if x >=50 and x %2==0:
  above50.append(x)
  print(above50)
  


##program 3

marks2=[25,11,65]
total = 0
for x in marks2:
 print(x)

for x in  marks2:
 total = total +x
 print(total) 



 ##progeam 3

 names=["snehal","chinmay","sayli","mani"]

# print(names)
# for nam in names:
#  print(nam)

for i in names:
  print("hello-welcome-"+ i)




