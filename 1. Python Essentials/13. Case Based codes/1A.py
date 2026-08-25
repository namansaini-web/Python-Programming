subject = []
for i in range(1,6):
    marks = int(input("Enter your marks od subject " + str(i) + ": "))
    subject.append(marks)
print(subject)
print()

avg = sum(subject)/len(subject)
print("Average marks : ", avg)

grade = ""
if avg >= 90:
    grade = "A"
elif avg >= 75:
    grade = "B"
elif avg >= 60:
    grade = "C"
else :
    grade = "D"
print("Grade : ", grade)

h = max(subject)
l = min(subject)
print("Highest marks : ", h)
print("Lowest marks : ", l)






