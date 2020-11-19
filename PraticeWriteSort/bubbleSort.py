def bubbleSort(data):
    for i in range(len(data)-1):
        swaped = False
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                print('{} swaped with {}'.format(data[j],data[j+1]))
                data[j],data[j+1]=data[j+1],data[j]
            swaped = True
        if not swaped :
            break


data = list(map(int,input('Enter Input : ').split(' ')))
bubbleSort(data)
print(data)