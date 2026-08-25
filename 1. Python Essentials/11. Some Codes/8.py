# Write a code to find the sum of all even numbers in a list:

def fun(values):
    total_even = 0
    total_odd = 0
    for v in values:
        if v%2 == 0 :
            total_even += v
        else:
            total_odd += v
    return total_even, total_odd

numbers = [2,5,7,12,16]
print(fun( numbers ))

