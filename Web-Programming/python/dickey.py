student = {
    "name" : "ayesha_imtiaz",
     "subject" : {
         "phy" : 98,
         "chem" : 78,
         "math":45
     }
}
#keys 

print(student.keys())
print(list(student.keys()))

print(len(student))

#values 
print(student.values())
print(list(student.values()))

#items  -> return key values pairs
pairs  = list(student.items())
print(pairs[0])

#get -> return the key according to value
print(student.get("name")) #no error 
print(student.get("subject")) 

#update
student.update({"city" : "dehli", "age" : 16})

print(student)
