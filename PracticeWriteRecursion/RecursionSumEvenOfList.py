a = 0
def sumEven_list(data):
    if len(data) == 1 :
        if data[0] % 2 == 0:
            return data[0]
        else :
            return 0
    else :
        if data[0] % 2 == 0:
            return data[0] + sumEven_list(data[1:])
        return sumEven_list(data[1:]) 

data = list(map(int,input('Enter List : ').split())) 
print(sumEven_list(data))
