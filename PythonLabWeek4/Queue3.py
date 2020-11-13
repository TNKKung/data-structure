class Queue :
    def __init__(self,item=None):
        if item == None :
            self.item = []
        else :
            self.item = item
    def push(self,item):
        self.item.append(item)
    def pop(self):
        return self.item.pop(0)
    def size(self):
        return len(self.item)
    def peek(self):
        return self.item[-1]
    def isEmpty(self):
        return self.item == []
    def getItem(self):
        return self.item[0::]
datastring,datainteger = input('Enter String and Code : ').split(',')
integer = list(map(int,datainteger))
string = list(datastring)
cloneString = string
queueStr = Queue()
queueInt = Queue(integer)

for item in cloneString :
    if item == " ":
        string.remove(item)
for item in string :
    sum = 0
    if (item >= 'A' and item <= 'Z'):
        if (ord(item)+queueInt.item[0]) > 90:
            sum = (ord(item)+queueInt.item[0]) - 90
            queueStr.push(chr(64 +sum))
            queueInt.push(queueInt.pop())
        else :
            queueStr.push(chr(ord(item)+queueInt.item[0]))
            queueInt.push(queueInt.pop())

    if (item >= 'a' and item <= 'z'):
        if (ord(item)+queueInt.item[0]) > 122:
            sum = (ord(item)+queueInt.item[0]) - 122
            queueStr.push(chr(96 + sum))
            queueInt.push(queueInt.pop())
        else :
            queueStr.push(chr(ord(item)+queueInt.item[0]))
            queueInt.push(queueInt.pop())

print('Encode message is : ',queueStr.item)
print('Decode message is : ',string)

        

