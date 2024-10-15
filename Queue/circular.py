class Circular_queue:
    def __init__(self, size):
        self.queue = [None] * size 
        self.start = 0
        self.end = 0
        self.size = 0

    def isFull(self):
        if self.size == len(self.queue):
            return True
        else:
            return False
    
    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
        
    def enqueue(self, data):
        if self.isFull():
            return print('Queue is full!')
        else:
            self.queue[self.end] = data
            self.end += 1
            self.end = self.end % len(self.queue)
            self.size += 1
            return print(data, 'added')

    def dequeue(self):
        if self.isEmpty():
            return print('Queue is empty!') 
        else:
            data = self.queue[self.start]
            self.start += 1
            self.first = self.start % len(self.queue)
            self.size -= 1
            print(data, 'removed!')
    
    def display(self):
        if self.isEmpty():
            print('Queue is empty!')
        else:
            i = self.start
            while True:
                print(self.queue[i], end=' -> ')
                i += 1
                i %= len(self.queue)
                if i == self.end:
                    break


cq = Circular_queue(6)
cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.enqueue(60)

cq.dequeue()
cq.enqueue(45)
cq.enqueue(45)

cq.display()


