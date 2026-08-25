marks=[90,78,67,84]
print(marks)
a=["Naman" ,67 ,"string"]
print(a)

print(type(marks))
print(type(a))


# INDEXING:

print(marks[0])
print(a[2])

n = len(marks)
print(n)
print(marks[n-2]) 
print(marks[-2])


# Updating an element :

marks[2] = 99.9984
print(marks[2])


# More Concepts :
l = [9,8,7,6,5,4,3,2,1]

print(sorted(l)) #Doesn't modify the original list

l.sort() # Modify the original list 
print(l)


num = [5,10,15]
num[1] = num[0] + num[2]
print(num)
print(sum(num))

mark = [ 50,60,70,80]
for i in range(len(marks)) :
    mark[i] = mark[i] + 5
print(mark)   

data = [2,4,6]
for i in range(len(data)):
    print(i, data[i])

items = [1,2,3]
for i in range(len(items)) :
    items[i] = items[i] + 2
print(sum(items))    

values = [4,8,12]
i = 0
while i < len(values) :
    print(values[i] // 2)
    i +=1