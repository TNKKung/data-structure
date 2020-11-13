def findMaximum(l):
    if len(l) == 1:
       return l[0]
    else:
    #    minNumber = findMinimum(l[1:])
    #    min = l[0]
    #    if minNumber < min:
    #         min = minNumber
    #    return min

        # return findMaximum(l[1:]) if findMaximum(l[1:]) > l[0] else l[0] 
        
        return max(l[0],findMaximum(l[1:]))

data = inp = list(map(int, input('Enter Input : ').split()))
print(findMaximum(data))
