class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

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
            print(data, 'deleted')
            return

        prev = self.head
        curr = self.head.next
        while curr:
            if curr.data == data:
                prev.next = curr.next
                if curr == self.tail:  
                    self.tail = prev
                print(data, 'deleted')
                return
            prev, curr = curr, curr.next

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

ll.delete(12)
print(ll.head.data, ll.tail.data)
ll.display()
