def binary_search(data,item):
    first = 0
    last = len(data)-1
    found = False
    while first <= last and not found :
        mid = (first + last) // 2
        if data[mid] == item :
            found = True 
        else :
            if data < data[mid]:
                last = mid - 1
            else :
                first = mid + 1
    return found

data = input('Enter Input : ').split('/')
print(binary_search(data[0],data[1]))
