def selectionSort(data,n):
    if len(data) == 1 :
        return data
    else :
        maxValues = max(data[:n+1])
        print('{} equal {}'.format(data[data.index(maxValues)],data[n]))
        data[data.index(maxValues)] = data[n]
        data[lenght] = maxValues
    selectionSort(data,n-1)

data = list(map(int,input('Enter Input : ').split(' ')))
selectionSort(data,len(data)-1)
print(data)
        