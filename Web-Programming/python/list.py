marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))
#marks[0], marks[1]
print(marks[0])
print(marks[1])
print(len(marks))

student = ["ayesha", 87.9, 17, "Lahore"]
print(student[0])
student[0] = "saba"
print(student)

# string are immutable we cannot change it
str = "hello"
print(str[0])

#list method
# append() method 
list = [2,1,3]
list.append(4)
print(list)
list.append(5)
print(list)

#sort() function 
print(list.sort())
print(list)

#reverse order sorting 
print(list.sort(reverse=True))
print(list)

fruitlist = ["banana", "apple", "litchi"]
print(list.sort())
print(list)
fruitlist.append("orange")
print(fruitlist)

#reverse method 
charlist = ['a','b','c','d','e','f']
list.reverse()
print(list)

#insert method 
lists = [2,1,3]
lists.insert(1,5)
print(lists)

#remove method 
lists.pop(2)
print(lists)
