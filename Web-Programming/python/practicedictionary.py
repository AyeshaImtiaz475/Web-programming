#q1 
dictionary = {
   "table": ["a piece of furniture", "list of facts & figures"],
   "cat" : "a small animal"
}
print(dictionary)

#q2
#python ->  1 -> 3 student 
# java -> 1 -> 3 student 
# c++ -> 1 -> 1 student 
# c -> 1 classroom -> 1 student 
# javascript -> 1 -> 1


subjects = {
    "python" , "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"
}

print(subjects)
print(len(subjects))

# q3 
sub = {}
sub["phy"] = 56
sub["chem"] = 45
sub["math"] = 30
print(sub)

marks = {}
x = int(input("enter phy :"))
marks.update({"phy" : x})

x = int(input("enter chem :"))
marks.update({"chem" : x})

x = int(input("enter math :"))
marks.update({"math" : x})
print(marks)

# q4 
values = {9, "9.0"}
print(values)

value = {
    ("float", 9.0),
    ("int", 9)
}
print(values)
