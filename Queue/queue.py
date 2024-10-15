class Queue:
    def __init__(self, n=None):
        self.queue = []
        self.n = n

    def enqueue(self, data):
        if self.n is not None:
            if len(self.queue) == self.n:
                return print('Queue is full!')
        self.queue.append(data)
        return print(data, 'added')
            
    
    def dequeue(self):
        if len(self.queue) == 0:
            return print('Queue is empty!')
        else:
            data = self.queue.pop(0)
            return print(data, 'Removed')
    
    def display(self):
        print(self.queue)


que = Queue(7)
i = 0
while i < 10:
    que.enqueue(i)
    i += 1

que.display()

i = 0
while i < 10:
    que.dequeue()
    i += 1
que.display()
