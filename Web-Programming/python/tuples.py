#Tuples in python 
# A built-in data type that lets us create immutable sequences of values.

#Tuples are immutables like string: We cannot add new element and can't remove the element 

tup = (2,1,3,1)
#print(type(tup))
print(tup.index(2))
print(tup.count(2))

#accessing index values 
print(tup[0])
print(tup[1])

tuples = ()
print(tuples)
print(type(tuples))

tuple = (1.0)
print(tuple)
print(type(tuple))

#practice question 1
favouriteMovies = input("Enter your 3 favourite movies");
print(favouriteMovies)
userinput = favouriteMovies.split()
print("list of user inputs:", userinput)

#second method of doing this question
movies = []
mov1 = input("enter 1st movie: ")
mov2 = input("enter 2nd movie: ")
mov3 = input("enter 3rd movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)


#Check if a list contains a palindrome of elements.
list1 = ["m", "a", "a", "m"]
copy_list1 = list1.copy() #[1,2,1]
copy_list1.reverse()      #[1,2,1]

if(copy_list1 == list1):
    print("Palindrome")
else:
    print("Not a palindrome") 


#grade question 
grade = ["C", "D", "A", "A","B","B",'A']
grade.sort()
print(grade)
