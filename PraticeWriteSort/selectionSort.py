def selectionSort(data,n):
    if n == 0 :
        return data
    else :
        maxValues = max(data[:n+1])
        print('{} equal {}'.format(data[data.index(maxValues)],data[n]))
        data[data.index(maxValues)] = data[n]
        data[n] = maxValues
    selectionSort(data,n-1)

Data = [int(i) for i in input('Enter Input : ').split()]
selectionSort(Data,len(Data)-1)
print(Data)