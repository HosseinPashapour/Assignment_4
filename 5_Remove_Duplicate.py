numbers = []

m = int(input("enter number of numbers in your list: "))
print ("")
print ("Now, you should enter the numbers.")

for i in range (m):
    n = float(input ("enter your number:"))
    numbers.append(n)

print ("your numbers list: ", numbers)

res = set (numbers)
print ("The list after removing duplicates:", res)
