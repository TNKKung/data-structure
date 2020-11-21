def binarySearch(start, stop,data, k):
    if start > stop:
        return False
    mid = (start + stop) // 2
    if k == data[mid]:
        return True
    if k < data[mid]:
        print('a')
        return binarySearch(start, stop-1,data, k)
    return binarySearch(start+1, stop,data, k)

inp = input('Enter Input : ').split('/')
data, k = list(map(int, inp[0].split())), int(inp[1])
print(binarySearch(0, len(data) - 1, sorted(data), k))
