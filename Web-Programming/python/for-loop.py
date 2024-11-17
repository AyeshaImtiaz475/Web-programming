# in order to traverse on the list then we will used the for loop
nums = [1 , 2, 3, 4, 5]
for val in nums:
    print(val)

veggies = ["potato", "brijal", "ladyfinger","cucumber"]
for el in veggies:
    print(el)

tup = (1,2,3,4,2,8,9)
for nums in tup:
    print(nums)

str = "apnacollege"
for ch in str:
    if(ch == 'o'):
        print("o found")
        break
    print(ch)
else:
    print("END")