#prime number
num1=int(input("enter number"))
sq_num1=int(num1**.5)+2
"""for each in range(2,sq_num1):
    if num1%each==0:
        print("number is not prime")
        break
    else:
        print("number is prime")"""
flag=0
for each in range(2,sq_num1):
    if num1%each==0:
        print("number is not prime")
        flag=1
        break
if flag==0:
    print("number is prime")
