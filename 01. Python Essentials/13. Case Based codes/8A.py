a = input("Enter your subjects : ")
b = input("Enter your subjects : ")
subs_1 = set(a.split())
subs_2 = set(b.split())
print(subs_1)
print(subs_2)

common_sub = subs_1 & subs_2 
print("Common Subjects for both students : ", common_sub)

only_subs1 = subs_1 - subs_2 
print("Subjects for student 1 only : ", only_subs1)

only_subs2 = subs_2 - subs_1
print("Subjects for student 2 only : ", only_subs2)