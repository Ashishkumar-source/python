text = input("enter a string: ")

s = text.lower()
print(s)
rev = s[::-1]
if(rev==s):
   
    print("It is a palindrome. ")

else:

    print("It is not a palindrome.")