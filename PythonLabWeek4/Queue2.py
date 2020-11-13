class Queue :
    def __init__(self,item=None):
        if item == None :
            self.item = []
        else :
            self.item = item
    def enqueue(self,item):
        self.item.append(item)
    def dequeue(self):
        return self.item.pop(0)
    def size(self):
        return len(self.item)
    def isEmpty(self):
        return self.item == []

beforeData = input('Enter Input : ').split(',')
data = [item.split(' ') for item in beforeData]
queueEs = Queue()
queueEn = Queue()
for item in data:
    if item[0] == 'EN' or item[0] == 'ES' :
        if item[0] == 'EN':
            queueEn.enqueue(item[1])
        if item[0] == 'ES':
            queueEs.enqueue(item[1])
    else :
        if queueEn.size() != 0 or queueEs.size() != 0:
            if not queueEs.isEmpty():
                print(queueEs.dequeue())
            else :
                print(queueEn.dequeue())
        else :
            print('Empty')    
