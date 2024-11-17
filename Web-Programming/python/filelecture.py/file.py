#Python can be used to perform operations on a file. (read & write)

#TYPES OF FILES
#text files: .txt, .docx, .log etc. (These file contain the data in the form of character)
#Binary files: .mp4, .mov, .png, .jpeg etc.

#Open , read & Close file 
#f = open("file_name", "mode")
# "file_name" : sample.txt, demo.docx
#"mode": r:read and w: write 

f = open("/Users/awanlaptop/Desktop/python/filelecture.py/demo.txt", "rt")
 #reading a file 
data = f.read(5)
print(data)
print(type(data))

line1 = f.readline()
print(line1)

line2 =f.readline()
print(line2)

line2 =f.readline()
print(line2)  #empty line
f.close()

#data = f.read()
#data = f.readline()

#writing a file 
#f = open("demo.txt", "w")
#f.write("this is a new line")

f = open("/Users/awanlaptop/Desktop/python/filelecture.py/demo.txt", "w")
f.write("I want to learn Django after 2 days")
f.write("\nThen i move to javascript")

f = open("/Users/awanlaptop/Desktop/python/filelecture.py/sample.txt", "w")
f.write("I am learning python to understand machine learning & CS50x")

f.close()
# r+ : overide the file text at the starting point  (no truncate)
# w+ : writing the file (truncate)
# a+ : read and append mode (no truncate)
# r : pen for reading
# w: open for writing, truncating teh file first
# x: create a new file and open it for writing 
# a: oepn for writing , appending at the end of teh file if it exists
#b : binary mode
# t: text mode(default)


#with syntax
with open("/Users/awanlaptop/Desktop/python/filelecture.py/demo.txt", "r") as f:
    data = f.read()
    print(data)

#with syntax close the file automatically

with open("/Users/awanlaptop/Desktop/python/filelecture.py/demo.txt", "w") as f:
    f.write("hello world!")

#Deleting a file 
#using os module 
#module(like a code library) is a file written by another programmer 

#pip install tensorflow: if the library was not installed in teh python and we have to install the library from internet 
#pip3 install tensorflow

#import os
#os.remove

import os
os.remove("/Users/awanlaptop/Desktop/python/filelecture.py/sample.txt")


