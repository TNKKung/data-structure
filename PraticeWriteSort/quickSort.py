def partition(data, start, stop):
    pivot_idx = start
    for i in range(start+1, stop+1):
        # print(i)
        if data[i] <= data[start]:
            # print('data[i] = {} data[start] = {}'.format(data[i],data[start]))
            pivot_idx += 1
            # print('Pivotl up -> {}'.format(data[pivot_idx]))
            data[i], data[pivot_idx] = data[pivot_idx], data[i]
            # print(data)
    data[pivot_idx], data[start] = data[start], data[pivot_idx]
    
    return pivot_idx

def quickSortRecursion(data, start, stop):
    if start >= stop:
        return
    # print('Data -> {} Start -> {} Stop -> {}'.format(data,start,stop))
    pivot_idx = partition(data, start, stop)
    quickSortRecursion(data, start, pivot_idx-1)
    quickSortRecursion(data, pivot_idx+1, stop)

def quick_sort(data, start=0, stop=None):
    if stop is None:
        stop = len(data) - 1

    return quickSortRecursion(data, start, stop)

data = [int(i) for i in input('Enter Input : ').split()]
quick_sort(data)
print(data)