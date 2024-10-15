class HashTables:
    def __init__(self, size=10, load_factor=.75):
        self.table_size = size
        self.curret_size = 0 
        self.load_factor = load_factor
        self.table = [[] for _ in range(self.table_size)]
    
    def __setitem__(self, key, value):
        index = self._hash(key)
        chain = self.table[index]

        for idx, element in enumerate(chain):
            if element[0] == key:
                chain[idx] == (key, value)
                return print(key, 'Updated with', value)
        chain.append((key, value))
        self.curret_size += 1
        print(key, 'added with', value)

        if self._current_load_factor() > self.load_factor:
            self._resize()
        return
    
    def __getitem__(self, key):
        index = self._hash(key)
        chain = self.table[index]

        for element in chain:
            if element[0] == key:
                return element[1]
        return 'Item not found!'
    
    def __delitem__(self, key):
        index = self._hash(key)
        chain = self.table[index]

        for idx, element in enumerate(chain):
            if element[0] == key:
                del chain[idx]
                return print(key, 'deleted')
        return print('Item not found')
    
    def insert(self, key, value):
        index = self._hash(key)
        chain = self.table[index]

        for idx, element in enumerate(chain):
            if element[0] == key:
                chain[idx] == (key, value)
                return print(key, 'Updated with', value)
        chain.append((key, value))
        self.curret_size += 1
        print(key, 'added with', value)

        if self._current_load_factor() > self.load_factor:
            self._resize()
        return
    
    def get_item(self, key):
        index = self._hash(key)
        chain = self.table[index]

        for element in chain:
            if element[0] == key:
                return element[1]
        return 'Item not found!'
    
    def delete_item(self, key):
        index = self._hash(key)
        chain = self.table[index]

        for idx, element in enumerate(chain):
            if element[0] == key:
                del chain[idx]
                return print(key, 'deleted')
        return print('Item not found')

    def display_all(self):
        print(self.table)
    
    def _current_load_factor(self):
        return self.curret_size / self.table_size

    def _hash(self, key):
        return hash(key) % self.table_size
    
    def _resize(self):
        print('Resizing your table!')
        old_table = self.table
        self.table_size *= 2
        self.curret_size = 0
        self.table = [[] for _ in range(self.table_size)]

        for chain in old_table:
            for key, value in chain:
                self.insert(key, value)
        return print('Resizing completed')


ht = HashTables()

ht.insert('thwahir', 21)

print(ht.curret_size)

print(ht.table)

print(ht.get_item('hadi'))

ht['muhammed'] = 12

del ht['muhammed']

print(ht['thwahir'])

ht.display_all()


    
        

        

