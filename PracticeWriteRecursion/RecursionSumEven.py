def SumEven(data):
    if data <= 0 :
        return 0
    elif data % 2 == 0 :
        return data + SumEven(data-1) 
    return SumEven(data-1)

data = int(input('Enter Integer : '))
print(SumEven(data))