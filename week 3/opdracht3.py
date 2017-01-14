__author__ = 'robbie'

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class BSTNode:
    def __init__(self, e = None):
        self.element = e
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.element)

    def search(self,e):
        current = self
        found = False
        while not found and current:
            if current.element < e:
                current = current.right
            elif current.element > e:
                current = current.left
            else:
                found = True
            if found:
                return current
            else:
                return None

    def rinsert(self,e):
        if e.element > self.element:
            if self.right is None:
                self.right = e
            else:
                self.right.rinsert(e)
        if e.element < self.element:
            if self.left is None:
                self.left = e
            else:
                self.left.rinsert(e)

    def rsearch(self, e):
        #is equal
        if self.element == e.element:
            return True
        #is lower
        if e.element < self.element:
            if self.left is not None:
                return self.left.rsearch(e)
            else:
                return False
        #is higher
        if e.element > self.element:
            if self.right is not None:
                return self.right.rsearch(e)
            else:
                return False

    def rmax(self):
        if self.right is None:
            return self.element
        return self.right.rmax()
class BST:
    def __init__(self):
        self.root = None

    def search(self, e):
        if self.root and e:
            return self.root.search(e)
        else:
            return None

    def insert(self, e):
        if self.root is None and e:
            self.root = e
        else:
            self.root.rinsert(e)

    def search(self, e):
        if self.root and e:
            return self.root.rsearch(e)

    def max(self):
        return self.root.rmax()

    def showLevelOrder(self):
        q = Queue()
        level = 1
        if self.root is not None:
            q.enqueue(self.root)

            while q.isEmpty() is False:
                row = []
                while q.isEmpty() is False:
                    row.append(q.dequeue())
                for elem in row:
                    if elem.left is not None:
                        q.enqueue(elem.left)
                    if elem.right is not None:
                        q.enqueue(elem.right)
                print('level' + str(level))
                print(row)
                level += 1

bst = BST()
bst.insert(BSTNode(8))
bst.insert(BSTNode(5))
bst.insert(BSTNode(4))
bst.insert(BSTNode(9))
bst.insert(BSTNode(18))
bst.insert(BSTNode(19))
bst.insert(BSTNode(72))
bst.insert(BSTNode(1))
bst.insert(BSTNode(56))
bst.insert(BSTNode(62))
bst.insert(BSTNode(61))
print(bst.search(BSTNode(6)))
print(bst.max())
bst.showLevelOrder()
