def mergeSort(data):
    if len(data) <= 1:
        return data
    mid = (len(data) + 1) // 2
    firstLeft = data[:mid]
    firstRight = data[mid:]
    firstLeft = mergeSort(firstLeft)
    firstRight = mergeSort(firstRight)
    return list(merge(firstLeft, firstRight))


def merge(firstLeft,firstRight):
    ListSort = []
    while len(firstLeft) != 0 and len(firstRight) != 0:
        if firstLeft[0] < firstRight[0]:
            ListSort.append(firstLeft[0])
            firstLeft.remove(firstLeft[0])
        else:
            ListSort.append(firstRight[0])
            firstRight.remove(firstRight[0])
    if len(firstLeft) == 0:
        ListSort = ListSort + firstRight
    else:
        ListSort = ListSort + firstLeft
    return ListSort

data = [int(i) for i in input('Enter Input : ').split(' ')]
print(mergeSort(data))