names = []
prices = []
for i in range(1,6):
    name = input("Enter your name : ")
    names.append(name)
    price = int(input("Enter price of that product : "))
    prices.append(price)
print(names)
print(prices)
print()

# 1:
print("Total bill amount : ", sum(prices))
a = max(prices)
print("Highest prices item : ", names[prices.index(a)],"-->", a  )
b = min(prices)
print("lowest priced item : ", names[prices.index(b)]), "-->", b
print()


# 2:
total_bill_amount = sum(prices)
print(total_bill_amount)
mx = prices[0]
mx_prd = ""
mn = prices[0]
mn_prd = ""

for i in range(5):
    if prices[i] > mx:
        mx_prd = names[i]
        mx = prices[i]
    elif prices[i] < mn:
        mn_prd = names[i]
        mn = prices[i]
print(mx_prd)
print(mn_prd)

    