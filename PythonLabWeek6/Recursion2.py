def ispalindrome(data):
    if len(data) < 2: 
        return True
    if data[0] != data[-1]: 
        return False
    return ispalindrome(data[1:-1])

inp = input('Enter Input : ')
data = list(inp)
if ispalindrome(data) == True :
    print( "'" + inp + "'" + ' is palindrome')
else :
    print( "'" + inp + "'" + ' is not palindrome')
