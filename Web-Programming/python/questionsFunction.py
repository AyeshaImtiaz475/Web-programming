#write a function to print the list len
cities = ["Lahore", "Islamabad", "Karachi", "Peshawar", "Quetta"]
heroes = ["thor", "ironman", "captain america"]

#question no 2
print(heroes[0], end=" ")
print(heroes[1], end=" ")
print(heroes[2], end=" ")


def print_len(list):
    print(len(list))

print(cities)
print_len(cities)
print(heroes)
print_len(heroes)


#factorial of a number 
def cal_fact(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(5)

# 1usd = 278 

def converter(usd_val):
    pkr_value = usd_val * 278
    print(usd_val, "USD =",pkr_value, "PKR")

converter(300)

#create the function to return the odd and even string by taking input from the users 
