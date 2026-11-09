n=int(input("Enter a number"))
if n<=0:
    for i in range(n):
        num=int(input("Enter number:"))
else:           
    temp=n
    brc=0
    number_of_the_digits(n,brc)
    sum=0
    c=0
    reverse=0    
    while temp>0:
        c=temp%10
        reverse=reverse+c*(10**brc)    
        sum+=c
        brc-=1
        temp=temp/10
    print("The sum of the digits is:\n",sum)        
    print("The reverse number of n is:\n",reverse)
    if reverse==n:
        print("The number is palindrom")
def number_of_the_digits(n,i):
    while n>0:
        n=n/10
        i+=1
    return i    
    