# Write a code to revese a given string
        # 1
name = "Naman_saini"
n = len(name)
for i in range(n):
    print(name[n-1-i] , end="")   #1
print()
print(name[ : :-1])               #2  
        # 2
word = "Python"
result = ""
for ch in word :
    result = ch + result
print(result)           


for i in range(n):
    print(name[i])


Name = "Naman"
for i in range(len(Name)):
    print(i , Name[i])  
i = 0
while i < len(Name):
    print(Name[i])
    i += 2      


# Find the number of vowels present in a word
Word = "Pythoncoding"
count = 0
for ch in Word :
    if ch in "aeiouAEIOU" :
        count += 1
print(count)       

Count = 0
for ch in Word :
    if ch == "o":
        Count +=1
print(Count) 


Words = "computer"
counts = 0
for ch in Words :
    if ch < "m" :   # check the Ascii value 
        counts += 1
        print(ch, end=" ")        
print(counts)   
     

star = "LEVEL"
same = 0
for i in range(len(star)) :     
    if star[i] == star[-(i+1)] :
        print(i, -(i+1), "-->", star[i], star[-(i+1)])
        same += 1
print(same)        

   