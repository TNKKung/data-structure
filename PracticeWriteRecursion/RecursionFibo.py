def Fibo(data):
    if data == 0 or data == 1:
        return data
    return Fibo(data-2) + Fibo(data - 1)
   

data = int(input('Enter Integer : '))
for i in range(data):
       print('{} -> {}'.format(data,Fibo(i)))