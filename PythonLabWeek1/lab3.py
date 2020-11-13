print("*** Reading E-Book ***")

a = str(input("Text , Highlight : "))

b = a.split(",")

for c in b[0] :
    if(c == b[1]) :
        print('['+ c + ']',end='')
    else :
        print(c,end='')