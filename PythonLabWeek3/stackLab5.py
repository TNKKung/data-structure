class Stack:
    def __init__(self,item = None) :
        if item == None :
            self.item = []
        else :
            self.item = item
    def push(self,item):
        self.item.append(item)
    def pop(self):
        return self.item.pop()
    def size(self):
        return len(self.item)
    def peek(self):
        return self.item[-1]
    def isEmpty(self):
        return self.item == []

print('******** Parking Lot ********')
data = input('Enter max of car,car in soi,operation : ').split(' ')
stack = Stack()
if data[1] != '0' :
    stack = Stack(list(map(int,data[1].split(','))))

if data[2] == "arrive":
    if stack.size() < int(data[0]):
        if int(data[3]) not in stack.item:
            stack.push(int(data[3]))
            print('car',data[3],'arrive! : Add Car',data[3])
        else :
            print('car',data[3],'already in soi')
    else :
        print('car',data[3],'cannot arrive : Soi Full')

if data[2] == 'depart':
    if stack.isEmpty():
        print('car',data[3],'cannot depart : Soi Empty')
    else :
        if int(data[3]) not in stack.item :
            print('car',data[3],'cannot depart : Dont Have Car',data[3]) 
        else :
            tempStack = Stack()
            while stack.peek() != int(data[3]):
                tempStack.push(stack.pop())
            stack.pop()
            while not tempStack.isEmpty():
                stack.push(tempStack.pop())
            print('car',data[3],'depart ! : Car',data[3],'was remove')
            
print(stack.item)

        