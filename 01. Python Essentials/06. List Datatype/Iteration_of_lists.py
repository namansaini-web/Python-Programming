marks = [89,87,94,67,79]

n = len(marks)
for i in range(n):
    print(marks[i])
for i in marks :
    print(i , end=" ")    


# Write a code to print the element at even indexes :
l = [1,2,3,4,5,6,7,8,9]
n1 = len(l)
for i in range(n1) :
    if i%2 == 0 :
        print(l[i])  


# Write a code to print all even element :
L = [1,2,3,4,5,6,7,8,9]
for i in L :
    if i%2 == 0 :
        print(i)  

print(max(L))        
print(min(L))


# Write a code to sum all the element of the list :
LL = [1,2,3,4,5,6,7,8,9]
sum = 0
for i in LL :
    sum = sum + i
print(sum)


# Write a code to find average of all the element :
LLL = [1,2,3,4,5,6,7,8,9]
sum1 = 0
n2 = len(LLL)
for i in LLL :
    sum1 = sum1 + i
print(sum / n2)

# Write a code which tells the number of elements greater then 4 :
nums = [2,4,6,8,10]
count = 0
for i in nums :
    if i > 4 :
        count += 1
print(count)    

# Write a code to find product of all the elements of  list :
numbers = [3,5,7]
result = 1
for n in numbers :
    result = result * n
print(result)    

# Write a code which print elements od the list in revese order :
lis = [1,4,6,8,3]
N = len(lis)
for i in range(N):
    lis[i] = lis[N-1-i]  # Negetive indexes
print(lis)

