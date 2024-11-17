#question no 1
#print the elements of the folloing list using a loop
list = [1,4,9,16,25,36,49,81,100]
print("loop started")
for val in list:
    print(val)
print("loop ended")


#question 2
nums = (1,4,9,16,25,36,49,81,100,81)
x = 81
idx = 0
for el in nums:
    if(el == x):
        print("number found at idx", idx)
        break
    idx += 1
   
    
