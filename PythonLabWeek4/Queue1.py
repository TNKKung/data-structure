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

inp = input('Enter Input : ').split(',')
data = [item.split(' ') for item in inp]
queue = Queue()
for item in data:
    if item[0] == 'E':
        queue.push(item[1])
        print('Add',item[1],'index is',queue.item.index(item[1]))
    else :
        if queue.isEmpty():
            print('-1')
        else :
            print('Pop',queue.pop(),'size in queue is',queue.size())
if queue.isEmpty():
    print('Empty')
else :
    print('Number in Queue is : ',queue.item)

           
