class Node:
    def __init__(self, data,next = None,prev = None):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.header = Node(None)
        self.tailer = Node(None)
        self.header.next = self.tailer
        self.tailer.prev = self.header

    def __str__(self):
        if not self.is_Empty():
            current =self.header.next
            out = ''
            out2 =''
            current2 = self.tailer.prev
            while current is not None:
                out +=str(current.data) + ' '
                current = current.next
            while current2 is not None:
                out2 +=str(current2.data) + ' '       
                current2 = current2.prev
            return out + '-> ' + out2
        else :
            return 'Empty'

    def is_Empty(self):
        return self.header.next is self.tailer
    
    def add_back(self,item):
        prev_node = self.tailer.prev
        new_node = Node(item)
        prev_node.next = new_node
        new_node.prev = prev_node
        self.tailer.prev = new_node
        new_node.next = self.tailer

    def size(self):
        count = 0
        current = self.header.next
        while current != self.tailer.data:
            current = current.next
            count += 1
        return count

    def index_of(self,item):
        count = 0
        current = self.header.next
        while current != self.tailer.data:
            if current.data == item :
                return count
            count +=1
            current = current.next
        return 

    def node_at(self,item):
        count = 0
        current = self.header.next
        while current is not self.tailer.data :
            if count == item :
                return current.data
            count += 1
            current = current.next
        return 

    def add_head(self,item):
        next_node = self.header.next
        new_node = Node(item)
        next_node.prev = new_node
        new_node.next = next_node
        self.header.next = new_node
        new_node.prev = self.header
        
    def pop_head(self):
        to_pop = self.header.next
        next_node = to_pop.next
        self.header.next = next_node
        next_node.prev = self.header
        to_pop.next = None
        to_pop.prev = None
        return to_pop.data

    # def pop_back(self):
    #     to_pop = self.tailer.prev
    #     prev_node = to_pop.prev
    #     self.tailer.prev = prev_node
    #     prev_node.next = self.tailer
    #     to_pop.next = None
    #     to_pop.prev = None
    #     return to_pop.data
    
    

    # def insert(self,data,index):
    #     if index == 0 or self.is_Empty():
    #         self.add_head(data)
    #     elif index >= self.size():
    #         self.add_back(data)
    #     else:
    #         new_node = Node(data)
    #         current = self.node_at(index)
    #         current.prev.next = new_node
    #         new_node.next = current
    #         new_node.prev = current.prev
    #         current.prev = new_node 

    # def pop(self,index):
    #     if 0 <= index < self.size() and not self.is_Empty():
    #         if index == 0:
    #             return self.pop_head()
    #         elif index == self.size():
    #             return self.pop_back()
    #         else:
    #             current = self.node_at(index)
    #             prev = current.prev
    #             next = current.next
    #             data = current.data
    #             prev.next = next
    #             next.prev = prev
    #             return data
    # def remove(self,item):
    #     if self.head.data == item :
    #         next_node = self.head.next
    #         next_node.prev = None
    #         self.head.next = None
    #         self.head = next_node
    #     elif self.tail.data == item :
    #         prev_node = self.tail.prev
    #         prev_node.next = None
    #         self.tail.prev = None
    #         self.tail = prev_node
    #     else :
    #         current = self.head
    #         while current != None :
    #             if current.data == item :
    #                 break
    #         current = current.next
    #         prev_node = current.prev
    #         next_node = current.next
    #         prev_node.next = next_node
    #         next_node.prev = prev_node
 
                

           
            
            
            
    
L = LinkedList()
L.add_back('a')
L.add_back('b')
L.add_back('c')
L.add_back('d')
L.add_back('e')
L.add_back('f')

L.add_head('tom')
print(L.pop_head())
print(L)

