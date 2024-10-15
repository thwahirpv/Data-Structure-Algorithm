class Stack:
    def __init__(self, n=None):
        self.stack = []
        self.n = n
    
    def push(self, data):
        if self.n is not None:
            if len(self.stack) == self.n:
                return print('Stack is full')
        self.stack.append(data)
        return print(data, 'added')

    def pop_e(self):
        if not self.stack:
            return print('Stack is empty!')
        else:
            data = self.stack.pop()
            return print(data, 'removed!')
    

stk = Stack()
i = 0

while i < 10:
    stk.push(i)
    i += 1

print(stk.stack)
i = 0
while i < 5:
    stk.pop_e()
    i += 1

print(stk.stack)


    
         