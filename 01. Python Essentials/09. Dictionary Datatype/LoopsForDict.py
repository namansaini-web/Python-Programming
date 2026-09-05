student = { "name":"Naman" , "age":17 ,"CGPA":9.8, "city":"Chandigarh"}

for i in student.keys():
    print(i)
for i in student.values():
    print(i)
for i in student.items():
    print(i)    
for i in student.items():
    print("key = ", i[0], ", value = ", i[1])

print("Numbers of key-value pairs is : ", len(student))  
    # Or #
count = 0
for key in student.keys():
    count += 1
print("Numbers of key-value pairs is : ", count)


marks = {"Maths":90 , "Science":84 , "English":95}
total = 0
for subject in marks.keys():
    total += marks[subject]
print("Total marks: ", total)


Student = {
    "Maths": 90,
    "Science": 80
}
Student["Total"] = 0
for key in Student:
    if key != "Total":
        Student["Total"] += Student[key]
print(Student["Total"])

