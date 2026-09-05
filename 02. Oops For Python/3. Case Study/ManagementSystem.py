students = [
    {'roll': 101, 'name': 'Rahul', 'age': 20, 'course': 'Python', 'marks': 85},
    {'roll': 102, 'name': 'Neha', 'age': 19, 'course': 'SQL', 'marks': 92},
    {'roll': 103, 'name': 'Amit', 'age': 22, 'course': 'Python', 'marks': 74},
    {'roll': 104, 'name': 'Priya', 'age': 21, 'course': 'AI', 'marks': 96},
    {'roll': 105, 'name': 'Rohan', 'age': 20, 'course': 'Python', 'marks': 67}
]


# Build a student mangement system which --> 
# [display student, search Student, Find Topper, Calculate Average, Exit]

def search(roll):
   for student in students:
        if student["roll"] == roll:
            print(student)
            return "Record Found"
        return "Not Found"

def class_topper(students):
    topper_marks = 0
    topper = {}
    for student in students:
        if(student["marks"] > topper_marks):
            topper_marks = student["marks"]
            topper = student["name"]
    return topper

while True:
    choice = int(input("Enter your choice : "))
    if choice == 1:
        for student in students:
            print(student)

    elif choice == 2:
        roll = int(input("Enter student Roll no. : "))
        print(search(roll))

    elif choice == 3:
        print("Class Topper is : ", class_topper(students))

    elif choice == 4:
        total = 0
        for student in students:
            total += student["marks"]
        print("Average : ", total/len(students))

    elif choice == 5:
        print("Thank You!")

    else:
        print("Invalid Choice")