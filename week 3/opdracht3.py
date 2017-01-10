__author__ = 'robbie'

class BinaryNode:

    def __init__(self,element=None,left=None,right=None):
        self.element = element
        self.left = left
        self.right = right

    def __repr__(self,nspaces=0):
        s1 = ''

        if self.right:
            s1 = self.right.__repr__(nspaces + 3)
        s2 = ' '*nspaces + str(self.element) + '\n'
        s3 = ''
        if self.left:
            s3 = self.left.__repr__(nspaces + 3)

        return s1 + s2 + s3

    def size(self):
        s = 1
        if self.left:
            s += self.left.size()
        if self.right:
            s += self.right.size()
        return s

    def height(self):
        if self.left:
            hleft = self.left.height()
        else:
            hleft = -1
        if self.right:
            hright = self.right.height()
        else:
            hright = -1
        return 1 + max(hleft,hright)

class BinaryTree:
    def __init__(self,root=None):
        self.root = root

    def __repr__(self):
        if self.root:
            return str(self.root)
        else:
            return 'null-tree'


    def size(self):
        if self.root:
            return self.root.size()
        else:
            return 0

    def height(self):
        if self.root:
            return self.root.height()
        else:
            return -1


def make_node(a):
    if not a:
        return None
    if len(a) == 1:
        return BinaryNode(a[0],None, None)

    mid = len(a)//2
    left_node = make_node(a[:mid])
    right_node = make_node(a[mid+1:])
    return BinaryNode(a[mid],left_node,right_node)

def make_tree(a):
    root = make_node(a)
    return BinaryTree(root)


a = [3,4,2,4,3,4,5,6]
tree = make_tree(a)

print(tree)