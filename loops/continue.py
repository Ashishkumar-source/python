# continue --- It is a loop control statement. It is used to skip the current iteration and move to the next iteration 
# without terminating the loop

i = 0
while i<=5:
    if(i%2==0):
        i+=1
        continue # it gives a skip 
    print(i)
    i+=1