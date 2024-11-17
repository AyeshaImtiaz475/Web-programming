#print numbers from 1 to 100

num = 1
print("loop started")
while ( num < 100):
    print(num)
    num += 1

print(num)
print("loop ended")

#print the number from 100 to 1

n = 100
print("loop started")
while (n > 1):
    print(n)
    n -= 1

print(n)
print("loop ended")

#print the table 
i = 1
n = int(input("enter number :"))
while i <= 10:
    print(n*i)
    i += 1

#print the list 
j= 1
print("loop started")
while j <= 10:
    print(j*j)
    j += 1

print(j)

print("loop ended")


#q4
nums = [1,4,9,16,25,36,49,81,100]
print("loop started")
idx=0
while idx < len(nums):
    print(nums[idx])
    idx += 1

print("loop ended")

#search for a number x in this tuple using loop
numlist = (1, 4, 9, 16, 25, 36, 49, 81, 100)
x = 36
z = 0
print("loop started")
while z < len(numlist):
    if(numlist[z] == x):
        print("found at index", z)
    z += 1

print("loop ended")
