class Queue :
    def __init__(self,item=None):
        if item == None :
            self.item = []
        else :
            self.item = item
    def enQueue(self,item):
        self.item.append(item)
    def deQueue(self):
        return self.item.pop(0)
    def size(self):
        return len(self.item)
    def isEmpty(self):
        return self.item == []
data1,data2 = input('Enter Input : ').split('/')
cloneData1 = data1.split(',')
cloneData2 = data2.split(',')
dataQueue = [item.split(' ') for item in cloneData1]
dataStaffQueue = [item.split(' ') for item in cloneData2]
dictOfQueueId = {}
for item in dataQueue :
    dictOfQueueId[item[1]] = item[0]
print(dictOfQueueId)
dictQueue = {}
for item in dataStaffQueue : 
    if item[0] == 'E':
        if dictQueue.get(dictOfQueueId[item[1]]) is None:
            dictQueue[dictOfQueueId[item[1]]] = Queue()
        dictQueue[dictOfQueueId[item[1]]].enQueue(item[1])
    else :
        if len(dictQueue) == 0 :
            print('Empty')
        else :
            key = list(dictQueue.keys())
            print(dictQueue[key[0]].deQueue())
            if dictQueue[key[0]].isEmpty():
                del dictQueue[key[0]]
