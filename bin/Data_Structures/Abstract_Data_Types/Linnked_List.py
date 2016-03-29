class Node:
    def __init__(self,init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self,data):
        self.data = data

    def set_next(self,node):
        self.next = node


class linked_list:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.get_data() == item:
                found = True
            else :
                current = current.get_next()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item:
                found = True
            else :
                previous = current
                current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else :
            previous.set_next(current.get_next())


#mylist =  linked_list()
#mylist.add(31)
#mylist.add(31)
#mylist.add(32)
#mylist.add(33)
#mylist.add(34)
#mylist.add(35)
#mylist.add(36)
#mylist.add(37)
#print mylist.search(37)
##print mylist.size()
#print mylist.remove(37)
#print mylist.size()
#temp = Node(93)mylist.add(31)
#print temp.get_data()