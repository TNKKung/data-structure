def findFactorial(data):
    if data <= 1 :
        return 1
    return data * findFactorial(data-1)

data = int(input('Enter Integer : '))
print(findFactorial(data))