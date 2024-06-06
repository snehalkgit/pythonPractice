# ##logical

# ##dict in list



students = [
    {
        "firstName":'snehal',
        "lastName":"kamble",
        "age":25,
        "rollNo":66,
        "skills":["python","javascript","sql"]

    }
    ,
    {
        "firstName":'sayli ',
        "lastName":"jogi",
        "age":22,
        "rollNo":74,
        "skills":["js","pyth","sql","css","html"]
    },
    {
        "firstName":'chinmay',
        "lastName":"deshpande",
        "age":34,
        "rollNo":8,
        "skills":["js","typescript","html","sql"]
    }
]


for student in students:
    print(student['firstName']+ student['lastName'])


#  for e.g snehal:3 skills 
for student in students:
 print(student['firstName']+ ":" + str(len(student['skills'])))


# program 3
# average age of all students 
totalage = 0
for student in students:
    totalage = totalage + student['age']
print(totalage/len(students))

##------------------------------
# add datascience skills to every student
for student in students:
    student['skills'].append('datascience')
print(students)

##-------------------------------------------

# country:"India"
for student in students:
    student['country'] = "india"
print(students)


#program 6
# names above >= 24

for student in students:
    if(student['age'] <25):
        print(student['firstName'])


        