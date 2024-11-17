str1 = "This is a string."
str2 = 'ApnaCollege'
str3 = """this is a string"""

str4 = "this is a tring.\n we are creating it in python"
print(str4)

# concatination
str5 = "apna"
str6 = "college"
final_str = str5+str6
print(final_str)

#length of str 
str7 = "ayesha"
len1 = len(str7)
print(len1)
# in length special character and spaces are count

#indexing 
str = "apna college"
ch = str[5]
print(ch)

#slicing: Accessing parts of a string 
# string [index : ending index] ending idx is not included 
print(str[3:8])
print(str[5:])
print(str[:4]) #[0:4]

#slicing: negative index -> backward counting 
mystr = "apple"
#A  P   P  L  E
#-5 -4 -3  -2 -1
print(mystr[-3:-1])

# string functions 
#endswith: returns true if string ends with substr
myownstr = "i am studing python from Apnacollege"
print(myownstr.endswith("ege"))
print(myownstr.endswith("app"))

#capitalize(): 1st character
print(myownstr.capitalize())
print(myownstr)

#str replace
print(myownstr.replace("python", "javascript"))

#find word: returns 1st index occurrence
print(myownstr.find("q"))

# str.count("am") : returns the count 
print(myownstr.count("o"))

#pracrice questions
name = input("my name is:")
print(name)
namelength = len(name)
print(namelength)

dollarstring = "Hello i had received dollar $. It's approximate $4567"
print(dollarstring.find("$"))



