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

inp = list(input('Enter Input : '))
listStack = Stack()
for i in inp:
    if(listStack.isEmpty()):
        listStack.push(i)
    else :
        if (listStack.peek() == '(' and i == ')' ) or (listStack.peek() == '[' and i == ']' ) :
            listStack.pop()
        else :
            listStack.push(i)

if listStack.size() == 0 :
    print(listStack.size())
    print('Perfect ! ! !')
else :
    print(listStack.size())



