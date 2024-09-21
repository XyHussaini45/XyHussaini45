import random
'''
1 is snake 
-1 is for water
0 is for gun'''
computer=random.choice([1,0,-1 ])
youstr=input("enter your choice : ")
youdict={"s" :1, "g" :0, "w" :-1}
revdict={1: "snake", -1 : "water" , 0 :"gun"}


you=youdict[youstr]

print(f"you chose {revdict[you]}/n computer chose{revdict[computer]}")


if(computer==you):
    print("DRAW")
    
    
else:
    if(computer==-1 and you==1):
        print("you win !!")
    elif(computer==0 and you==1):
        print("You win ")
    elif(computer==1 and you==0):
        print("You lose ")
    elif(computer==0 and you==1):
        print("You win ")
    elif(computer==0 and you==-1):
        print("You lose")

    elif(computer==1 and you==-1):
        print("You lose ")
        
    else:
        print("Something went wrong ")

