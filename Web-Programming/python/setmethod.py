collection = set()
#add
collection.add(0)
collection.add(1)
collection.add(2)
collection.add(3)
collection.add("helllo world")
print(collection)

#remove
collection.remove(1)
print(collection)

#unhashable -> lists, sets, dictionary those are immutable and after changes they give different output

#clear
# print(collection.clear())

#pop
print(collection.pop())

#set.union
#combines both set values & returns new value 

set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2)) #{1,2,3,4}
print(set1)
print(set2)


set3 = {11,22,33}
set4 = {22,33,44}
print(set3.intersection(set4)) #{1,2,3,4}
print(set3)
print(set4)
