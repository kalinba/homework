N=int(input("Enter a value for N:"))
if N<=0:
    print("Invalid number")
else:
    sum=0
    max=0
    i=0    
    while i < N:
        num=int(input(f"Enter the {i} number: "))
        if num%2==0:
            sum+=num
        elif num<max:
            min=num
        i+=1    
    if max==0:
        print("Yhere aren't odd numbers")        
    print("Sum of the even numbers is:",sum)
    print("The biggest number of the odd ones is:",max)        
                