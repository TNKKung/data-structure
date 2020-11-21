def binarySearch(data,k,start,stop):
    if start > stop:
        return 'No First Greater Value'
    if data[start] > k:
        return data[start]
    return binarySearch(data, k,start+1, stop)

def boubbleSort(lis,lenData): 
    for i in range(lenData-1): 
        for j in range(lenData-i-1): 
            if lis[j] > lis[j+1] : 
                lis[j], lis[j+1] = lis[j+1], lis[j]               
    return lis

inp = input('Enter Input : ').split('/')
data, k = list(map(int, inp[0].split())), list(map(int, inp[1].split()))
for i in k:
    print(binarySearch(boubbleSort(data,len(data)),i,0,len(data)-1))