def partition(data, start, stop):
    pivot_idx = start
    for i in range(start+1, stop+1):
        if data[i] <= data[start]:
            pivot_idx += 1
            data[i], data[pivot_idx] = data[pivot_idx], data[i]
    data[pivot_idx], data[start] = data[start], data[pivot_idx]
    
    return pivot_idx

def quickSortRecursion(data, start, stop):
    if start >= stop:
        return
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