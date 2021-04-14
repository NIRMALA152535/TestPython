"""print ("Last number not inclusive in range either in forward or backward range ")
print("Range " , list(range (2,10,2)))
print("Reverse ", list(range (10,2,-2)))"""

"""print ("for loop")
for each in range(10):
    print (each)

print ("for loop print in horiz fashion")
for each in range(10):
    print (each,end=",")"""


str1="python programming"
a=input("enter character")
i=0

print(str1.count(a))

for l in str1:
    print(l,end=" ")
    if a == l:
        i+=1
print( '\n',a , " occured ", i , " times ")