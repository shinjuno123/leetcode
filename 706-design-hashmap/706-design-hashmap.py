class ListNode:
    def __init__(self,value = None,next = None,key = None):
        self.value = value
        self.next = next
        self.key = key

from collections import defaultdict
        
class MyHashMap:

    def __init__(self):
        self.table = defaultdict(ListNode)
        self.k = 1000

    def put(self, key: int, value: int) -> None:
        index = key % self.k
        
        # if there was no initial node
        if self.table[index].value is None:
            node = ListNode(value=value,key=key)
            self.table[index] = node
            return
        
        start = self.table[index]
        
        while start:
            # if key already exists
            if start.key == key:
                start.value = value
                return
            if start.next is None:
                break
            
            start = start.next
        
        # if there was no key matching and also initial node
        start.next = ListNode(value=value,key=key)
        

    def get(self, key: int) -> int:
        index = key % self.k
        if self.table[index].value is None:
            return -1
        
        start = self.table[index]
        
        while start:
            if start.key == key:
                return start.value
            
            start = start.next
        
        return -1
        

    def remove(self, key: int) -> None:
        index = key % self.k
        
        if self.table[index].value is None:
            return
        
        start = self.table[index]
        
        if self.table[index].key == key:
            self.table[index] = ListNode() if self.table[index].next is None else start.next
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