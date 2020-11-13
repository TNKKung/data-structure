class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            curr = self.root
            while True:
                if data < curr.data:
                    if curr.left is None:
                        curr.left = Node(data)
                        break
                    curr = curr.left
                else:
                    if curr.right is None:
                        curr.right = Node(data)
                        break
                    curr = curr.right
        return self.root

    def print_tree(self, node, level=0):
        count_Left = 0
        count_Right = 0
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('     ' * level, node)
            self.print_tree(node.left, level + 1)

    def inorder(self, root):
        res = []
        if root:
            res = self.inorder(root.left)
            res.append(root.data)
            res = res + self.inorder(root.right)
        return res


if __name__ == '__main__':
    T = BST()
    inp1,inp2 = input('Enter Input : ').split('|')
    inp_1 =  [int(i) for i in inp1.split(' ')]
    for i in inp_1:
        root = T.insert(i)
    T.print_tree(root)
    print('--------------------------------------------------')
    print('Below '+ inp2 + ' :' ,end = ' ')
    a = T.inorder(root)
    b = []
    for i in a:
        if i < int(inp2):
            b.append(i)

    if b == [] :
        print('Not have')
    else :
        print(*b)