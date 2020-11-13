print('*** Odd Even ***')
a,b,c = input('Enter Input : ').split(',')

if a is 'S' :
    e = list(b)
    def odd_even(arr,s):
        if s == 'Odd' :
            for x in range(0,len(b),2) :
                print(b[x],end = '')
        else :
            for x in range(1,len(b),2) :
                print(b[x],end = '')
    odd_even(b,c)
    print()

if a is 'L' :
    e = b.split(" ")
    def odd_even(arr,s):
        if s == 'Odd' :
            print(e[::2])
        else :
            print(e[1::2])
    odd_even(b,c)
    print()

