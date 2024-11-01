first=int(input("Enter number: "))
operator=input("enter a operator (+,-,/,*,%) : ")
second=int(input("Enter a 2 number : "))

if operator=='+':
    print(first+second)
    
elif operator=='-':
    print(first-second)
    
elif operator=='/':
    print(first/second)
    
elif operator=='*':
    print(first*second)
    
elif operator=='%':
    print(first%second)
    
else:
    print("Invalid Operator ")
    