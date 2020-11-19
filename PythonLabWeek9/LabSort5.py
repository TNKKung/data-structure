# def bubbleSort(data):
#     for i in range(len(data)-1):
#         for j in range(len(data)-i-1):
#             if data[j] > data[j+1]:
#                 data[j],data[j+1] = data[j+1],data[j]

# def insertSort(data):
#     lis = []
#     for i in range(len(data)):
#         lis.append(data[i])
#         if len(lis) > 1 :
#             for j in range(len(lis)-1):
#                 if data[i] < data[j] :
#                     print('{} insert front {}'.format(data[i],data[j]))
#                     data.insert(j,data.pop(data.index(data[i])))
#                     print(data)

# def findResultOf(results,data):
#     listOfSum = []
#     for i in range(len(data)):
#         pass


# results,data = input('Enter Input : ').split('/')
# integerData = list(map(int, data.split()))
# # findResultOf(int(results),integerData)
# insertSort(integerData)
# print(integerData)

def boubleSort(sequence):
    for i in range(len(sequence)-1):
        swaped = False

        for j in range(len(sequence)-1-i):
            if sequence[j] > sequence[j+1]:
                swaped = True
                sequence[j], sequence[j+1] = sequence[j+1], sequence[j]

        if not swaped:
            break
    return sequence

def getPatternStorage(sequence, summation, curr_summation=0, index=0, pattern=None, pattern_storage=None):
    if pattern is None:
        pattern = []
    if pattern_storage is None:
        pattern_storage = []

    if curr_summation == summation:
        pattern_storage.append(list(pattern))
        return pattern_storage

    if index == len(sequence):
        return pattern_storage
    print('{} {} {} {} {} {}'.format(sequence, summation, curr_summation + sequence[index], index+1, pattern, pattern_storage))
    print() 
    pattern.append(sequence[index])
    getPatternStorage(sequence, summation, curr_summation + sequence[index], index+1, pattern, pattern_storage)
    print('{} {} {} {} {} {}'.format(sequence, summation, curr_summation + sequence[index], index+1, pattern, pattern_storage))

    print(pattern.pop())
    getPatternStorage(sequence, summation, curr_summation, index+1, pattern, pattern_storage)

    return pattern_storage

def sortPatterStorage(pattern_storage):
    for i in range(len(pattern_storage)-1):
        swaped = False

        for j in range(len(pattern_storage)-1-i):
            if len(pattern_storage[j]) > len(pattern_storage[j+1]):
                swaped = True
                pattern_storage[j], pattern_storage[j+1] = pattern_storage[j+1], pattern_storage[j]
        if not swaped:
            break
    return pattern_storage

### Main ###
summation, inputList = input('Enter Input : ').split('/')
summation = int(summation)
inputList = list(map(int, inputList.split()))

boubleSort(inputList)
patternStorage = getPatternStorage(inputList, summation)
sortPatterStorage(patternStorage)
if len(patternStorage) == 0:
    print("No Subset")
else:
    for pattern in patternStorage:
        print(pattern)