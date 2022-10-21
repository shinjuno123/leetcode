class Node:
    def __init__(self,key=None,value=None):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(Node)

    def put(self, key: int, value: int) -> None:
        index = key % self.size
        
        start = self.table[index]
        if start.value is None:
            self.table[index] = Node(key, value)
            return
        
        while start:
            if start.key == key:
                start.value = value
                return
            if start.next is None:
                break
            
            start= start.next
        
        start.next = Node(key, value)


    def get(self, key: int) -> int:
        index = key % self.size
        
        if self.table[index].value is None:
            return -1
        
        start = self.table[index]
                
        while start:
            if start.key == key:
                return start.value
            
            start = start.next
        
        return -1
        

    def remove(self, key: int) -> None:
        index = key % self.size
        
        
        if self.table[index].value is None:
            return
        
        start = self.table[index]
        
        if start.key == key:
            self.table[index] = start.next if start.next is not None else Node()
            return
        
        prev = start
        
        while start:
            if start.key == key:
                prev.next = start.next
                return
            
            start, prev = start.next, start
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)