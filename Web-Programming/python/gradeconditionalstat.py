marks = int(input("marks: "))
if marks >= 90:
    print("A")
elif marks >= 80 and marks < 90:
    print("B")
elif marks >= 70 and marks < 80:
    print("C")
else:
    print("D")

#nesting 
age = 34
if(age >= 18):
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else: 
    print("cannot drive")

#practice questions 
userinput = int(input("enter the number:"))
print(userinput)
if(userinput% 2 == 0):
    print("even no")
else:
    print("odd number")


userinput2 = int(input('enter the number that is multiple of 7:'))
print(userinput2)
if(userinput2 % 7 == 0):
    print("number is multiple of 7")
else: 
    print("no is not multiple of 7")



a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))

if(a >= b and a >= c):
    print("first number is largest", a)
elif(b>=c and b>=a):
    print("second number is largest", b)
else:
    print("third is largest", c)


num1 = int(input("enter first number:"))
num2 = int(input("enter the second number:"))
num3 = int(input("enter the third number:"))
num4 = int(input("enter the fur number:"))

if(num1>=num2 and num1>=num3 and num1>=num4):
    print("first number is largest", num1)
elif(num2>=num1 and num2>=num3 and num2>=num4):
    print("second number is greater than all number", num2)
elif(num3>=num1 and num3>=num2 and num3>=num4):
    print("third number is greater than all number", num3)
else:
    print("four number is greater than all number", num4)