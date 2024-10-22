class BST:
    def __init__(self, data=None):
        self.data = data
        self.leftchld = None
        self.rightchld = None
    
    def insert(self, data):
        if self.data is None:
            self.data = data
            print(data, 'Inserted at Root')
            return 
        if data < self.data:
            if self.leftchld:
                self.leftchld.insert(data)
                return 
            self.leftchld = BST(data)
            print(data, 'Inserted')
            return 
        elif data > self.data:
            if self.rightchld:
                self.rightchld.insert(data)
                return
            self.rightchld = BST(data)
            print(data, 'Inserted')
            return 
        else:
            print(data, 'Already inserted, Duplicate data not allowed!')
            return 
    
    def search(self, data):
        if self.data is None:
            print('Binary search is empty!')
            return 
        
        if data == self.data:
            print(data, 'Founded')
            return self
        if data < self.data:
            if self.leftchld:
                self.leftchld.search(data)
                return 
            print(data, 'Not found!')
            return
        elif data > self.data:
            if self.rightchld:
                self.rightchld.search(data)
                return
            print(data, 'Not found!')
            return
    
    def count(self, node):
        if node is None:
            return 0
        return 1+self.count(node.leftchld)+self.count(node.rightchld)    
        
    def delete(self, data, current=None, is_first_call=True):
        if self.data is None:
            print('Binary search is empty!')
            return
        
        if is_first_call:
            if self.count(current) <= 1:
                print("You can't delete", data,"tree have only one data")
                return

        if data < self.data:
            if self.leftchld:
                self.leftchld = self.leftchld.delete(data, is_first_call=False)
            else:
                print(data, 'is not found!')
        elif data > self.data:
            if self.rightchld:
                self.rightchld = self.rightchld.delete(data, is_first_call=False)
            else:
                print(data, 'is not found!') 
        else:
            if self.leftchld is None:
                temp = self.rightchld
                if current is not None:
                    if current.data == data:
                        current.data = temp.data
                        current.leftchld = temp.leftchld
                        current.rightchld = temp.rightchld
                        temp = None
                        return
                self = None
                return temp
            elif self.rightchld is None:
                temp = self.leftchld
                if current is not None:
                    if current.data == data:
                        current.data = temp.data
                        current.leftchld = temp.leftchld
                        current.rightchld = temp.rightchld
                        temp = None
                        return
                self = None
                return temp
            node = self.rightchld
            while node.leftchld:
                node = node.leftchld
            self.data = node.data
            self.rightchld = self.rightchld.delete(node.data, is_first_call=False)
        return self

    def preorder_traverse(self):
        if self.data is None:
            print('Binary search is empty!')
            return
        
        print(self.data, end=' ')
        if self.leftchld:
            self.leftchld.preorder_traverse()
        if self.rightchld:
            self.rightchld.preorder_traverse()
        
    def inorder_traverse(self):
        if self.data is None:
            print('Binary search is empty!')
            return

        if self.leftchld:
            self.leftchld.inorder_traverse()
        print(self.data, end=' ')
        if self.rightchld:
            self.rightchld.inorder_traverse()
    
    def post_order(self):
        if self.data is None:
            print('Binary search is empty!')
            return

        if self.leftchld:
            self.leftchld.post_order()
        if self.rightchld:
            self.rightchld.post_order()
        print(self.data)
    
    def min_node(self):
        if self.data is None:
            print('Binary search is empty!')
            return
        
        node = self.leftchld
        while node.leftchld:
            node = node.leftchld
        print(node.data)
        return node
    
    def max_node(self):
        if self.data is None:
            print('Binary search is empty!')
            return
        
        node = self.rightchld
        while node.rightchld:
            node = node.rightchld
        print(node.data)
        return node
    
    def colse_value(self, target):
        if self.data is None:
            print('Binary search is empty!')
            return

        closest = self.data
        current = self
        while current:
            if abs(current.data - target) < abs(closest - target):
                closest = current.data
            
            if target < current.data:
                current = current.leftchld
            elif target > current.data:
                current = current.rightchld
            else:
                break
        return closest
    
    def is_binary(self, root, low=float('-inf'), height=float('inf')):
        if not root:
            return True
        
        if root.data <= low and root.data >= height:
            return False
        
        return (self.is_binary(root.leftchld, low, root.data) and self.is_binary(root.rightchld, root.data, height))
        

        

        

root = BST()
arr = [50,40,45,30,23,25,45,80,70,60,58,90,94,98,100]
for data in arr:
    root.insert(data)
root.inorder_traverse()

print()
root.max_node()

demo = root.is_binary(root)
print(demo)
