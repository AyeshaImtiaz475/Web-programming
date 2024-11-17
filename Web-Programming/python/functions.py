#Functions in Python 
#Block of statments that perform a specific task 

#function definition through a keyword which is (def)
#function definition
def calc_sum(a,b):  #paraneters
    sum = a+b
    print(sum)
    return sum

#calling a functions; arguments 
calc_sum(13,4)


def mult_num(x,y):
    multiple=x*y
    print(multiple)
    return multiple

#calling a function
print("Multiplcation of two number :")
mult_num(5,6)


#print hello
def print_hello():
    print("hello world!")

output = print_hello()
print(output)  #None
print_hello()


#Averge of three number
def average_num(c,d,e):
    num_sum = c + d +e 
    average= num_sum/3
    print(average)
    return average

average_num(12,4,5)


#Build in function 
#if we want to print the strings in a single line then we have to at end with space
print("apncollege", "ayeshaImtiaz", end= " ") #sep=" "
print("I am learning python language") #end="/n"

#len(): give the length of the container 
#type()
#range 
#range(start, stop, step)

#default parameters 
def cal_prod(p=1,q=1):
    print(p*q)
    return p*q
cal_prod()
