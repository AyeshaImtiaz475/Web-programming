#create a new file "practice.txt"
#with open("/Users/awanlaptop/Desktop/python/filelecture.py/practice.txt", "w") as f:
   # f.write("Hi everyone\n we are learnig file I/O\n")
   # f.write("using Java.\n I like pramming in java.")


#write the function that replaces all occureneces "java" with "python"

with open("/Users/awanlaptop/Desktop/python/filelecture.py/practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("Java", "Python")
print(new_data)

#serach if the world "learning" exits in teh file or not

word = "learning"
with open("/Users/awanlaptop/Desktop/python/filelecture.py/practice.txt", "r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("Found")
    else:
        print("not found")

def check_for_line():
    word = "learning"
    data = True  # starting iteration we want to run the dara 
    line_no =1   # line is 1 at the starting 
    with open("/Users/awanlaptop/Desktop/python/filelecture.py/practice.txt", "r") as f:
        while data:
            data = f.readline()
            if(word in data):  #find till the data is valid 
                print(line_no)
            line_no += 1       # if the word was not found then check for the next line 
            #if the word doesn't exits then return -1

    return -1
print(check_for_line())


#question 3
with open("/Users/awanlaptop/Desktop/python/filelecture.py/practice.txt", "r") as f:
    data = f.read()

    num = ""
    for i in range(len(data)): #loop will run till the data length
        if(data[i] == ","):
            print(int(num))
            num = ""
        else:
            num += data[i]
