# CSV File ==>

import csv

with open("student.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Marks", "City"])
    writer.writerow(["Naman", 90, "Chandigarh"])

with open("student.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

name = input()
marks = int(input())
city = input()
with open("student.csv", "a", newline="") as file:
    data = csv.data(file)
    data.append(["Ishan", 65, "Jhanjeri"])
