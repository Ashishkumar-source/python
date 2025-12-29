nums =[1,4,3,25,5,36,49,81,64,100,36]
n =int(input("enter the number to check : "))

i = 0 #initiliation
while i<len(nums):
    if(nums[i]==n):
        print("found at index ",i)
        break
    i+=1