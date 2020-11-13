checkGoMax = False
checkGoMin = False
checkEQ = False
def FindData(data):
    global checkGoMax
    global checkGoMin
    global checkEQ
    if data[0] > data[1]:
        for i in range(len(data)-1):
            if data[i] > data[i+1] :
                checkGoMin = True
            if data[i] == data[i+1]:
                checkEQ = True
            if data[i] < data[i+1]:
                checkGoMax = True
        return
    if data[0] < data[1]:
        for i in range(len(data)-1):
            if data[i] > data[i+1] :
                checkGoMin = True
            if data[i] == data[i+1]:
                checkEQ = True
            if data[i] < data[i+1]:
                checkGoMax = True
        return
    if data[0] == data[1]:
        for i in range(len(data)-1):
            if data[i] > data[i+1] :
                checkGoMin = True
            if data[i] == data[i+1]:
                checkEQ = True
            if data[i] < data[i+1]:
                checkGoMax = True
        return


data = list(map(int,''.join(input('Enter Input : ')))) 
FindData(data)
if checkGoMax == True and checkEQ == False and checkGoMin == False :
    print('Metadrome')
elif checkGoMax == True and checkEQ == True and checkGoMin == False :
    print('Plaindrome')
elif checkGoMax == False and checkEQ == False and checkGoMin == True :
    print('Katadrome')
elif checkGoMax == False and checkEQ == True and checkGoMin == True :
    print('Nialpdrome')
elif checkGoMax == False and checkEQ == True and checkGoMin == False :
    print('Repdrome')
else :
    print('Nondrome')


