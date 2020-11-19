def insertSort(data):
    for i in range(1,len(data)):
        j = i-1
        temp = data[i]
        while data[j] > temp and j >=0 :
            data[j+1] = data[j]
            j = j-1
        data[j+1] = temp

Data = [int(i) for i in input('Enter Input : ').split()]
insertSort(Data)
print(Data)