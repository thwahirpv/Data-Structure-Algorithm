class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None  
    
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node  
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node   

        print(data, 'added')
        return

    def search(self, data):
        curr = self.head
        while curr:
            if curr.data == data:
                print(data, 'found')
                return data
            curr = curr.next

        print(data, 'not found!')
        return None

    def delete(self, data):
        if self.head is None:
            print('Linked list is empty!')
            return
        
        if self.head.data == data:
            self.head = self.head.next
            if self.head is None:  
                self.tail = None
            else:
                self.head.prev = None
            print(data, 'deleted')
            return
 
        curr = self.head.next
        while curr:
            if curr.data == data:
                if curr == self.tail:  
                    self.tail = curr.prev
                    self.tail.next = None
                else:
                    curr.prev.next, curr.next.prev = curr.next, curr.prev
                print(data, 'deleted')
                return
            curr = curr.next

        print(data, 'not found!')
        return

    def display(self):
        if self.head is None:
            print('Linked list is empty!')
            return

        curr = self.head
        while curr:
            print(curr.data, end=' -> ')
            curr = curr.next
        
        print()
        return

    def reverse_display(self):
        if self.tail is None:
            print('Linked list is empty!')
            return
        
        curr = self.tail
        while curr:
            print(curr.data, end=' -> ')
            curr = curr.prev
        
        print()
        return


ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(45)
ll.insert(56)
ll.insert(23)
ll.insert(78)
ll.insert(12)

print(ll.head.data, ll.tail.data)
ll.display()

ll.search(45)

ll.delete(10)
print(ll.head.data, ll.tail.data)
ll.display()
ll.reverse_display()
