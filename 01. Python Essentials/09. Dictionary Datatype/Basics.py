student = { "name":"Naman" , "age":17 , "city":"Chandigarh"}
print(student)
print(type(student))
print(student["name"])

# modification:
student["age"] = 18
print(student)

# Adding new key:
student["CGPA"  ] = 9.8
print(student)

# Non error method: if key is not present in dict then,
#                  it will not give error and say none.
print(student.get("city"))

print(student.get("address"))  
print(student.get("address", "Key not found"))

# To delete a key-value:
student.pop("CGPA")
print(student)