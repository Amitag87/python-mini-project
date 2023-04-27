import random
level=input("for beginner level type B ; for medium level type M ; for hard level type H")
a=random.randint(1,100)

if level=="B":
    attempt=5
    for i in range(attempt):
        n=int(input("enter a value"))
        if n==a:
         print("Congratulations! you have won this game")
         break
        elif n<a:
          print("your entered no. is too small")
          attempt-=1
        else:
           print("your entered no. is too big")
           attempt-=1
        if attempt==0:
            print("game ended \nbetter luck next time")
        
elif level=="M":
    attempt=3
    for i in range(attempt):
        n=int(input("enter a value"))
        if n==a:
         print("Congratulations! you have won this game")
         break
        elif n<a:
          print("your entered no. is too small")
          attempt-=1
        else:
         print("your entered no. is too big")
         attempt-=1
        if attempt==0:
            print("game ended \nbetter luck next time")
    
elif level=="H":
    n=int(input("enter a value"))
    if n==a:
        print("Congratulations! you have won this game")
        
    else:
        print("game ended \nbetter luck next time")
        
