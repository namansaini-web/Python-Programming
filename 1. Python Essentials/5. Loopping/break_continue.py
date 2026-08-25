# Break Statement :

for i in range(1,21) :
  if (i == 11) :
    break
  print(i) 

for i in range(1,10,2):
   if i == 6 :
      break
   print(i)   


# Continue Statement :
for i in range(1,11):
   if(i == 5):
      continue 
   print(i)


#Print all even numbers between 1 to 10 using continue statement
for i in range(1,11):
   if(i % 2 != 0) :
      continue
   print(i)   


for i in range(10):
   if( i % 3 == 0 ):
      continue
   print(i)


x = 7
while x > 0 :
   if( x == 4 ):
      break
   print(x)
   x -= 1


for a in "Python" :
   if( a == "h") :
      continue
   print(a)


i = 1
while i <= 5 :
   if i == 3 :
      i += 1
      continue
   print(i)
   i += 1


