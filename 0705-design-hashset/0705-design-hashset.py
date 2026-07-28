class LinkedList:
    def __init__(self, key=-1, next=None):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        self.maps = [LinkedList() for i in range(1000)]

    def Hash(self, key:int):
        return key%len(self.maps)

    def add(self, key: int) -> None:
        curr = self.maps[self.Hash(key)]
        while curr.next:
            if curr.next.key == key:
                return
            curr = curr.next
        curr.next = LinkedList(key)
        

    def remove(self, key: int) -> None:
        curr = self.maps[self.Hash(key)]
        while curr and curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next
        return 
        

    def contains(self, key: int) -> bool:
        curr = self.maps[self.Hash(key)].next
        while curr:
            if curr.key == key:
                return True
            curr = curr.next
        return False

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)