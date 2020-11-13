n = int(input("Enter Input : "))

for x in range(n+1) :
    for y in range((n+2)-(x+1)) :
        print(".",end="")
    for y in range((x+1)) :
        print("#",end = "")
    for y in range ((n+2)) :
        if((x == 0 or x == x+1)or(y == 0 or y == n+1)) :
            print("+",end="")
        else :
            print("#",end = "")
    print()
for x in range((2*n+4)) :
    if(x <= n+1) :
        print("#",end = "")
    else :
        print("+",end = "")
print()

for x in range((2*n+4)) :
    if(x <= n+1) :
        print("#",end = "")
    else :
        print("+",end = "")
print()  

for x in range(n,-1,-1) :
    for y in range(n+2) :
        if(x == 0 or y==0 or y == n+1) :
            print("#",end = "")
        else :
            print("+",end = "")
    for y in range((x+1)) :
        print("+",end = "")
    for y in range((n+2)-(x+1)) :
        print(".",end="")
    print()
    
