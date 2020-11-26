def insertSort(data):
    for i in range(1,len(data)):
        j = i-1
        tmp = data[i]
        while data[j] > tmp and j >= 0 :
            data[j+1] = data[j]
            j = j-1
        data[j+1] = tmp

data = [int(i) for i in input('Enter Input : ').split(' ')]
insertSort(data)
print(data)

