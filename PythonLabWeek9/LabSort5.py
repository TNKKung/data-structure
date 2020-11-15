def bubbleSort(data):
    for i in range(len(data)-1):
        for j in range(len(data)-i-1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]

def insertSort(data):
    lis = []
    for i in range(len(data)):
        lis.append(data[i])
        if len(lis) > 1 :
            for j in range(len(lis)-1):
                if data[i] < data[j] :
                    print('{} insert front {}'.format(data[i],data[j]))
                    data.insert(j,data.pop(data.index(data[i])))
                    print(data)

def findResultOf(results,data):
    listOfSum = []
    for i in range(len(data)):
        pass


results,data = input('Enter Input : ').split('/')
integerData = list(map(int, data.split()))
# findResultOf(int(results),integerData)
print(integerData)
