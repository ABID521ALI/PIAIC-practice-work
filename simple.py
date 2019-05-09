print("simple Calculator")
a=int(input("Enter 1st Number: "))
b=int(input("Enter 2nd Number: "))
c=(input("Enter Opertion: "))
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/':
    print(a/b)
else:
    print("Invalid Operation")    
