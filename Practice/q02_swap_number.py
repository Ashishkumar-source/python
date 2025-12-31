a = int(input("enter the number: "))
b = int(input("enter the number: "))

print("before swaping a = " , a, ", b = ",b)

# declare a new variable 
temp = a # store value of a in temp 
a=b
b=temp

print("after swapping a = ",a,", b = ",b)