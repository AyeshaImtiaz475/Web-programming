info = {
    "key" : "value",
    "name": "apnacollege",
    "learning": "coding",
    "age": 35,
    "is_adult" : True,
    "marks" : 95.98
}
print(info)

studyChannel = {
    "name" : "apnacollege",
    "subjects": ["python", "C", "Java"],
    "topics" : ("dict","set"),
    "age" : 35,
    "is_adult" : True,
    "market" : 94.4,
     12: 12.56
}
print(studyChannel)
print(type(studyChannel))

print(info["name"])
print(studyChannel["is_adult"])

# print(info("surname"))
info["name"] = "saba"
print(info)

null_dic = {}
null_dic["name"] = "pwskills"
print(null_dic)


# Dictories are mutable 
# It is used to create the data values in key:values pairs 
# It don't allow duplicate keys & they are unordered

# Nested doctionaries

student = {
    "name" : "ayesha_imtiaz",
     "subject" : {
         "phy" : 98,
         "chem" : 78,
         "math":45
     }
}
print(student)
print(student["subject"]["chem"])
print(student["name"])

