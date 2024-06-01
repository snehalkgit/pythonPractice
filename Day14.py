##program 1

vehicle={
    "color":"white",
    "model":"altrozxz",
    "reg":151545
    }


print(vehicle)
print(vehicle["reg"])


##key value

for x in vehicle:
    print(vehicle[x])


for x in vehicle.keys():
    print(x)

for x in vehicle.values():
    print(x)


for x in vehicle.items():
    print(x)   


for key,value in vehicle.items():
    print(key,value)


vehicle.pop('reg')
print(vehicle)
##removing elements


# vehicle["city"] = "mumbai"
# print(vehicle)


vehicle['expiry']=['2030']
print(vehicle)



rowone={"1":"one","2":"two","3":"three"}
rowtwo={"4":"four","5":'five'}

rowone.update(rowtwo)
print(rowtwo)
print(rowone)

  ## will set new value if not present 
vehicle.setdefault("city","goa")
print(vehicle)
vehicle.setdefault("city")
print(vehicle)




a1 = vehicle.fromkeys(["six","seven"])
print(a1)