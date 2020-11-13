def findPalindrome(data):
    if len(data) == 2 :
        return True
    else :
        if data[0] != data[-1] :
            return  False
    return findPalindrome(data[1:-1])

data = input('Enter String : ')
print(findPalindrome(data))