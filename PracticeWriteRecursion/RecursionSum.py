def sum(data):
    if data == 0 :
        return 0 
    return data + sum(data-20)

# def check_sum(n):
#     return int(n*(n+1)/2)
# check_sum(1000)

data = int(input('Enter Integer : '))
print(sum(data))