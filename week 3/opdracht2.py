__author__ = 'robbie'

class ListNode:
    def __init__(self,data,next_node):
        self.data = data
        self.next = next_node

    def __repr__(self):
        return str(self.data)


class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        s = ''
        current = self.head
        if current != None:
            s = s + str(current)
            current = current.next
        while current != None:
            s = s + " -> " + str(   current)
            current = current.next
        if not s: # s == '':
            s = 'empty list'
        return s

    def addLast(self,e):
        if not self.head: # self.head == None:
            self.head = ListNode(e,None)
            self.tail = self.head
        else:
            n = ListNode(e,None)
            self.tail.next = n
            self.tail = self.tail.next

    def delete(self,e):
        if self.head: # self.head != None:
            if self.head.data == e:
                self.head = self.head.next
                if self.head == None:
                    self.tail = None
            else:
                current = self.head
                while current.next != None and current.next.data != e:
                    current = current.next
                if current.next != None:
                    current.next = current.next.next
                if current.next == None:
                    self.tail = current


class MyCircularList:

    def __init__(self):
        self.tale = None

    def __repr__(self):
        r = ""
        if self.tale is not None:
            r += str(self.tale)
            r += "\n"
            nextNode = self.tale
            while nextNode.next != self.tale:
                nextNode = nextNode.next
                r+= str(nextNode) + "\n"
        return r

    def append(self, e):
        if self.tale is None:
            self.tale = ListNode(e, None)
            self.tale.next = self.tale
        else:
            nextNode = self.tale
            while nextNode.next != self.tale:
                nextNode = nextNode.next
            nextNode.next = ListNode(e, self.tale)

    def delete(self, e):
        if self.tale is not None:
            if self.tale.data == e:
                if self.tale.next != self.tale:
                    currentNode = self.tale
                    while currentNode.next != self.tale:
                        currentNode = currentNode.next
                    self.tale = self.tale.next
                    currentNode.next = self.tale
                else:
                    self.tale = None
            currentNode = self.tale
            while currentNode.next.data != e and currentNode.next != self.tale:
                currentNode = currentNode.next
            if currentNode.next.data == e:
                currentNode.next = currentNode.next.next

linkedList = MyLinkedList()
circularList = MyCircularList()
circularList.append(1)
circularList.append(2)
circularList.append(3)
circularList.append(4)
circularList.append(5)
circularList.append(6)
circularList.append(7)
circularList.append(8)
circularList.append(9)
circularList.append(10)

circularList.delete(8)
circularList.delete(7)
print(circularList)