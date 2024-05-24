# ternary operator ---- 
# program 1 
a = 10
b = 5

if a > b:
    print("a is greater")
else:
    print("b is greater")
print("a is greater") if a > b else print("b is greater")

# program 2
age = 16
f = "can drive" if age >= 17 else "cannot drive"
print(f)


age = 18
ageA = "can drive"if age>=18 else "cannot drive"
print(ageA)


##program 3 

##loop

#range is used for loops

##range(stratindex,endindex,stepsize)

##endvalue can not be considered

##print 0 to 5
for x in range(0,6):
    print(x)


 ##print table of 2 

for x in range(2,21):
    print(x)

##table of 2 in reverse
for x in range(20,0,-2):
    print(x)


for x in range(3,33,3):
 print(x)

 ##1 to 10
 for x in range(1,11):
  print(x)


  # program 
# break statment and continue statment with for
# break immediately halt the loop


for x in range(1,5):
   if a ==4:
      break
   print(x)



for x in range(2,15):
   print(x)
   if a ==10:
    break
   

for x in range(1,12,3):
 if a ==5:
    break
 print(x) 



 for x in range(20,1,-2):
    print(x)



##continue
for a in range(10):
    if a == 8:
        continue
    print(a)
   
for x in range(12,2,-2):
   if a ==10:
      break
   print(x)

for x in range(20):
   if b == 10:
      continue
   print(x)
   

for x in range(10,16):
   if a == 5:
      break
   print(x)