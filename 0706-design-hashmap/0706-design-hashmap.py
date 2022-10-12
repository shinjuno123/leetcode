class Node:
    def __init__(self,value = None,key = None):
        self.value = value
        self.key = key
        self.next = None

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.table = collections.defaultdict(Node)

    def put(self, key: int, value: int) -> None:
        hashed_key = key % self.size
        
        if self.table[hashed_key].value is None:
            self.table[hashed_key] = Node(value, key)
            return
        
        start = self.table[hashed_key]
        prev = start
        while start:
            if start.key == key:
                start.value = value
                return
            
            prev, start = start, start.next
        
        prev.next = Node(value,key)

    def get(self, key: int) -> int:
        hashed_key = key % self.size
        
        if self.table[hashed_key].key == key:
            return self.table[hashed_key].value
        
        start = self.table[hashed_key]
        
        while start:
            if start.key == key:
                return start.value
            
            start = start.next
        
        return -1

    def remove(self, key: int) -> None:
        hashed_key = key % self.size
        
        start = self.table[hashed_key]
        if start.key == key:
            self.table[hashed_key] = Node() if start.next is None else start.next
            return
        
        prev = start
        start = start.next
        while start:
            if start.key == key:
                prev.next = start.next
                return
            prev,start = start, start.next
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)