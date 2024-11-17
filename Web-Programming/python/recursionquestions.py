#write a recursion function to calcualte the sum of n natural number 

def calc_sum(n):
    if(n == 0):  #base case 
        return 0
    return calc_sum(n-1) +n #recursive function

sum = calc_sum(10)  
print(sum)   #printing the value 


#write a recusrive function to print all the elements in the list 
def print_list(list,idx=0):
    if(idx == len(list)):  #base case
        return
    #print the list and its index value
    print(list[idx])
    print_list(list, idx+1)  #recursive function


fruits = ["mango", "banana", "orange", "apple"]
print_list(fruits)
