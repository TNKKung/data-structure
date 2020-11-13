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

inp = input('Enter Input : ').split(',')
data = [item.split(' ') for item in inp]
stack = Stack()
for item in data :
    if item[0] == 'A' :
        if (stack.isEmpty()):
            stack.push(int(item[1]))

        else :
            while not stack.isEmpty() and int(item[1]) >= stack.peek() :
                stack.pop() 
            stack.push(int(item[1]))
    else :
        print(stack.size())
        