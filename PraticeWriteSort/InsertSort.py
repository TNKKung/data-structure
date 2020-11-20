def insertSort(data):
    for i in range(1,len(data)):
        j = i-1
        tmp = data[i]
        while data[j] > tmp and j >= 0 :
            data[j+1] = data[j]
            j = j-1
        data[j+1] = tmp
    # return data
# def insertSortlist(data):
#     lis = []
#     for i in range(len(data)):
#         lis.append(data[i])
#         if len(lis) > 1 :
#             for j in range(len(lis)-1):
#                 if data[i] < data[j] :
#                     print('{} insert front {}'.format(data[i],data[j]))
#                     data.insert(j,data.pop(data.index(data[i])))
#                     print(data)

data = [int(i) for i in input('Enter Input : ').split(' ')]
insertSort(data)
print(data)

