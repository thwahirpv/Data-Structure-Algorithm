class Node:
    def __init__(self):
        self.children = dict()
        self.end = False
    

class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = Node()
            current = current.children[letter]
        current.end = True
    
    def search(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                print(word, 'Not found!')
                return False
            current = current.children[letter]
        if current.end:
            print(word, 'Found!')
            return current.end
        else:
            print(word, 'Not found!')
            return current.end
    
    def startWith(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True

    def delete(self, word):
        def _delete(current, index):
            if index == len(word):
                if current.end is False:
                    print(word, 'Not found!')
                    return False
                current.end = False
                return len(current.children) == 0
            
            if word[index] not in current.children:
                print(word, 'Not found!')
                return False
            
            current_node = _delete(current.children[word[index]], index+1)
            if current_node:
                del current.children[word[index]]
                return len(current.children) == 0 and current.end is False
            return False
        _delete(self.root, 0)

                



        

        
trie = Trie()
trie.insert('samual')
trie.insert('sam')
trie.insert('apple')

trie.delete('samual')

print(trie.search('samual'))




