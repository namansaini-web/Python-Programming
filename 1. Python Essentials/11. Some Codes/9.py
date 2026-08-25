# Print the subjects in a list where the marks scored are atleast 85:

student = {
    "maths": 80,
    "science": 90,
    "english": 85,
    "social-science": 95,
    "hindi": 70
}
Sub = []

for subject in student:
    if student[subject] >= 85:
        Sub.append(subject)
print(Sub)