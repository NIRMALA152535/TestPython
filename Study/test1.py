#marks >=90 A 80 B 70 C
num1=int(input("Enter the marks "))
#num1=int(num1)
print(num1, type(num1))
if num1 >=90:
    grade="A"
elif num1 >=80:
    grade="B"
elif num1 >=70:
    grade="C"
elif num1 >=60:
    grade="D"
else:
    grade="E"
#print (f"{grade}")
 print(f" The marks of student is {num1} and the grade is {grade}")

