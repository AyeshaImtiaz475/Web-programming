i = 0
while( i <= 5):
    if( i == 3):
        i += 1
        continue
    print(i)
    i += 1

j = 1
while j <= 10:
    if(j%2 == 0):
        j += 1
        continue #skip
    print(j)
    j += 1

   # 1 3 5 7  9 