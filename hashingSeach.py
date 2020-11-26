class Data:
    def __init__(self,key,value):
        self.key = key
        self.value = value
    
    def __str__(self):
        return "({0}, {1})".format(self.key,self.value)

class hash:
    def __init__(self,table_size,max_collision):
        self.tableSize = table_size
        self.maxCollision = max_collision
        self.tableData = []
        for i in range(table_size):
            self.tableData.append(None)
    def get_hash(self,string):
        indexData = 0
        for i in string: 
            indexData += ord(i)
        return indexData % self.tableSize

    def is_Full(self):
        indexData = 0
        for i in range(len(self.tableData)):
            if self.tableData[i] is not None:
                indexData += 1
        return indexData == self.table_size

    def add_data(self,data):
        if self.is_Full() :
            print('This table is full !!!!!')
            quit()
        key, value = data.key,data.value
        retry = 0
        hashed_index = self.get_hash(key)
        while retry < self.max_collision:
            index = (hashed_index + retry ** 2) % self.tableSize
            if self.tableData[index] is None :
                self.table[index] = data
                return 
            retry += 1
            print(f'collision number {retry} at {index}')
        print('Max of collisionChain')