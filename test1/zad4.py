a=int(input("Enter a value for a: "))
b=int(input("Enter a value for b: "))
if a<=0 or b<=0:
    print("Invalid numbers")
else:
    nod=0
    while b>0:
        temp=b
        b=a%b
        a=temp
    nod=a
    print("\nThe lowest own divider of a and b is: ",nod)
    if nod==1:
        print("числата са взаимно прости")
    else:print("Не са взаимно прости")    
    nok=(a*b)//nod
    print("\nnok of a and b is:",nok )