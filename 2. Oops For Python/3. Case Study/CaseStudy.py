students = [
    {'roll': 101, 'name': 'Rahul', 'age': 20, 'course': 'Python', 'marks': 85},
    {'roll': 102, 'name': 'Neha', 'age': 19, 'course': 'SQL', 'marks': 92},
    {'roll': 103, 'name': 'Amit', 'age': 22, 'course': 'Python', 'marks': 74},
    {'roll': 104, 'name': 'Priya', 'age': 21, 'course': 'AI', 'marks': 96},
    {'roll': 105, 'name': 'Rohan', 'age': 20, 'course': 'Python', 'marks': 67}
]

# Print only the names of all students.
for student in students:
    print(student["name"])

# Calculate the total marks obtained by all students.
total = 0
for student in students:
    print(student["marks"])
    total += student["marks"]
print("Toatal marks obtained : ", total)

# Find Average Marks of the class
total = 0
n = len(students)
for student in students:
    print(student["marks"])
    total += student["marks"]
print("Average marks : ", total/n)

# Count Passed Students
# Pass Marks = 40
count = 0
for student in students:
    if student["marks"] >= 40:
        count += 1
print(count)

# Write a function to Print Grade of Every Student
# 90+ --> A , 75+ --> B , 60+ --> C , else --> D
def calc_grade(marks):
    if marks > 90:
        grade = "A"
    elif marks > 75:
        grade = "B"
    elif marks > 60:
        grade = "C"
    else:
        grade = "D"
    return grade
print("Marks"," ","Grade")
for student in students:
    print(student["marks"],"      ", calc_grade(student["marks"]))


# Create a function to Search Student by their Roll Number
def search(roll_no):
   for student in students:
        if student["roll"] == roll_no:
            print(student)
            return "Record Found"
        return "Not Found"

roll = int(input())
ans = search(roll)
print(ans)


# Write a function to print the topper of the class:
def class_topper(students):
    topper_marks = 0
    topper = {}
    for student in students:
        if(student["marks"] > topper_marks):
            topper_marks = student["marks"]
            topper = student
    return topper


Ans = class_topper(students)
print(Ans)


# Count Students in each course:
courses = {}
for student in students:
    if student["course"] not in courses:
        courses[student["course"]]  = 1
    else:
        courses[student["course"]] += 1
print(courses)


# remove duplicate courses:
course = []
for student in students:
    course.append(student["course"])
s = set(course)
print("Coruses in students : ", s)


# Create Student class (OPP) in the pattern of students:
class Student():
    def __init__(self, roll, name, age, course, marks):
        self.roll = roll
        self.name = name
        self.age = age
        self.course = course
        self.marks = marks

    def show_student(self):
        print(self.roll, self.name, self.age, self.course, self.marks)

s1 = Student(106, "MJ", 30, "Dance", 100)
s1.show_student()


        

