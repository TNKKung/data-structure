class Node:
    def __init__(self, data,next = None,prev = None):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def __str__(self):
        if not self.is_Empty():
            current =self.head
            out = ''
            while current is not None:
                out +=current.data + ' '
                current = current.next
            return out
        else :
            return 'Empty'

    def is_Empty(self):
        return self.head is None
    
    def add_back(self,item):
        if self.is_Empty():
            self.head=self.tail=Node(item)
        else:
            new_Node = Node(item)
            new_Node.prev = self.tail
            self.tail.next = new_Node
            self.tail = new_Node

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current =  current.next
        return count

    def index_of(self,item):
        count = 0
        current = self.head
        while current != None :
            if current.data == item :
                return count
            count +=1
            current = current.next
        return -1

    def node_at(self,item):
        count = 0
        current = self.head
        while current is not None :
            if count == item :
                return current
            count += 1
            current = current.next
        return -1

    def add_head(self,item):
        if self.is_Empty():
            self.head=self.tail=Node(item)
        else :
            new_Node = Node(item)
            new_Node.next = self.head
            self.head.prev = new_Node
            self.head = new_Node

    def pop_head(self):
        data = self.head.data
        next_node = self.head.next
        if self.head.next is not None:
            next_node.prev = None
            self.head.next = None
            self.head = next_node
        return data

    def pop_back(self):
        data = self.tail.data
        prev_node = self.tail.prev
        if self.tail.prev is not None:
            prev_node.next = None
            self.tail.prev = None
            self.tail = prev_node
        return data

    def insert(self,data,index):
        if index == 0 or self.is_Empty():
            self.add_head(data)
        elif index >= self.size():
            self.add_back(data)
        else:
            new_node = Node(data)
            current = self.node_at(index)
            current.prev.next = new_node
            new_node.next = current
            new_node.prev = current.prev
            current.prev = new_node 

    def pop(self,index):
        if 0 <= index < self.size() and not self.is_Empty():
            if index == 0:
                return self.pop_head()
            elif index == self.size():
                return self.pop_back()
            else:
                current = self.node_at(index)
                prev = current.prev
                next = current.next
                data = current.data
                prev.next = next
                next.prev = prev
                return data
    def remove(self,item):
        if self.head.data == item :
            next_node = self.head.next
            next_node.prev = None
            self.head.next = None
            self.head = next_node
        elif self.tail.data == item :
            prev_node = self.tail.prev
            prev_node.next = None
            self.tail.prev = None
            self.tail = prev_node
        else :
            current = self.head
            while current != None :
                if current.data == item :
                    break
            current = current.next
            prev_node = current.prev
            next_node = current.next
            prev_node.next = next_node
            next_node.prev = prev_node

    def reverse(self):
        current = self.tail
        string = ''
        while current != None:
            string += current.data + ' '
            current = current.prev

        return string
                
 
L = LinkedList()
L.add_back('a')
L.add_back('b')
L.add_back('c')
L.add_back('d')
L.add_back('e')
L.add_back('f')

print(L.reverse())


