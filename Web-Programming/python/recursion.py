#Recursion
#When a function calls itself repeatedly.

def show(n):
    if(n == 0):  #basecase
        return 
    print(n) #kaam 
    show(n-1) #calling for 5, 4; n-1, 3: n-2, 2: n-3, 1
    print("Call Stack END")

#calling the function to print the result 
show(5) 

#call stack
#When a varaible was declare or function was call the call stack will reserved the layer
#When ever we call the show function for n value like 1,2,3,4,5 
#the layer will be reserved in the call stack 

#When ever the base case function is hit then it return 
#First in call stack we move from bttom to top 
#after return we return the value from top -> bottom 


#factorial of a number 
def fact(n):
    if(n == 0 or n == 1):  #base case 
        return 1
    else:
        return fact(n-1)*n #recursive relations
    
print("The factorial of a number is:")
print(fact(6))