def genarate(data,List):
    if data == 0 :
        if len(List) == 0 :
            print('0')
        else :
            print('\n'.join(List))
    else :
        if len(List) == 0:
            return genarate(data-1,['0','1'])
        else :
            return genarate(data-1,['0' + i for i in List ] + ['1' + i for i in List])

data = int(input('Enter Integer : '))

genarate(data,[])

