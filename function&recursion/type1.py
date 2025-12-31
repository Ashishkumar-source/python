# 1. built in function.
# 2. User defined function.

print("apna college",end=" ")
print("upes")

def calc_multi(a=1,b=1): # function created by programmer. 
    multi=a*b
    print(multi)
    return multi
calc_multi()

# function with no agrument.
def greet():
    print("hello")
greet()

# keyword argument function 
def details(name,age):
    print(name,age)
details(age=20,name="ashish choudhary")