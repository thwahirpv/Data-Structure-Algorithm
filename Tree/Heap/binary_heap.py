class MinHeap:
    def __init__(self, limit):
        self.heap_list = [0] * limit
        self.limit = limit
        self.size = 0
    
    def getParentIndex(self, index):
        return (index - 1) // 2
    
    def getLeftChildIndex(self, index):
        return (2 * index) + 1
    
    def getRightChildIndex(self, index):
        return (2 * index) + 2
    
    def hasParent(self, index):
        return self.getParentIndex(index) >= 0
    
    def hasLeftChild(self, index):
        return self.getLeftChildIndex(index) < self.size
    
    def hasRightChild(self, index):
        return self.getRightChildIndex(index) < self.size
    
    def parent(self, index):
        return self.heap_list[self.getParentIndex(index)]
    
    def leftChild(self, index):
        return self.heap_list[self.getLeftChildIndex(index)]
    
    def rightChild(self, index):
        return self.heap_list[self.getRightChildIndex(index)]
    
    def isFull(self):
        return self.limit == self.size
    
    def swap(self, parentIndex, childIndex):
        self.heap_list[parentIndex], self.heap_list[childIndex] = self.heap_list[childIndex], self.heap_list[parentIndex]

    def heapifyUp(self):
        index = self.size  - 1
        while self.hasParent(index) and self.parent(index) > self.heap_list[index]:
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)
        return

    def heapifyDown(self):
        index = 0
        while self.hasLeftChild(index):
            smallValueIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.rightChild(index) < self.heap_list[smallValueIndex]:
                smallValueIndex = self.getRightChildIndex(index)
            if self.heap_list[index] < self.heap_list[smallValueIndex]:
                break
            else:
                self.swap(index, smallValueIndex)
                index = smallValueIndex

    def insert(self, data):
        if self.isFull():
            raise('Heap is full!')
        
        self.heap_list[self.size] = data
        self.size += 1
        self.heapifyUp()
        return print(data, 'Inserted')
    
    def removeMin(self):
        if self.size == 0:
            raise('Heap is empty!')
        data = self.heap_list[0]
        self.heap_list[0] = self.heap_list[self.size-1] 
        self.heap_list[self.size-1] = 0
        self.size -= 1
        self.heapifyDown()
        return data
    
    def display(self):
        index = 0
        while index < self.size:
            print(self.heap_list[index], end=' ')
            index += 1
        

mh = MinHeap(20)
list = [4,2,3,1,5,10,23,24,54]
for i in list:
    mh.insert(i)
mh.display()
print()
mh.removeMin()
print(mh.leftChild(3), mh.rightChild(3))
mh.display()
        

