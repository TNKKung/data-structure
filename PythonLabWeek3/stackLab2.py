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
    def getItem(self):
        return self.item[0::]
    def getIndexItem(self,index):
        return self.item[index]
        
sum = 0
inp = input("Enter Input : ").split(',')
data = [list(map(int,item.split())) for item in inp]
platStack = Stack()
for item in data:
    if (platStack.isEmpty()):
        platStack.push(item)
    else :
        while not platStack.isEmpty() and item[0] > platStack.peek()[0] :
            print(platStack.pop()[1])
        platStack.push(item)        






        






