#range function returns a sequence of numbers, starting from 0 by default, and incremnets 
# by 1(by default), and stops before a specified number.

seq = range(5)
print(range(0))
print(range(1))
print(range(2))
print(range(3))
print(range(4))

seq = range(10)

for i in seq:
    print(i)

# range(start?, stop, step?) 
for i in range(2,10,2):
    print(i)

for i in range (2,101,2):
    print(i)

