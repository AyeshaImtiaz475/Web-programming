# find the sum of first natural numbers (using while)
n = 5
sum =0
for i in range(1, n+1):
    sum += i

print("sum is ", sum)

#multiiplciation of the numbers
num = 5
mul = 1
for i in range(1, num+1):
    mul *= i

print("multiplication of number :", mul)

#factorial of a number 
#factorial n = 5

mynum = 5
fact = 1
i = 1
while i<= mynum:
    fact *= i
    i+= 1

print(fact)