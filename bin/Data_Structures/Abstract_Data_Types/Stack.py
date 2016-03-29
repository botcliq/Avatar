class Stack():
    def __init__(self):
        self.items= []

    def is_empty(self):
        return self.items == []

    def push(self,item):
        self.items.append(item)

    def peek(self):
        return self.items[-1]

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Queue():
    def __init__(self):
        self.items= []

    def is_empty(self):
        return self.items == []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

# Completed implementation of a deque ADT
class Deque():
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0,item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


#q = Queue()
##q.enqueue('hello')
#q.enqueue('dog')
#q.enqueue(3)
#q.dequeue()

#print q.size()

#s = Stack()
#print(s.is_empty())
#s.push(4)
#s.push('dog')
#print(s.peek())
#s.push(True)
#print(s.size())
#print(s.is_empty())
#s.push(8.4)
#print(s.pop())
#print(s.pop())
#print(s.size())
