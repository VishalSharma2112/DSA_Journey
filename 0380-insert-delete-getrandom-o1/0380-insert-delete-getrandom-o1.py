import random
class RandomizedSet:

    def __init__(self):
        self.pos = {}
        self.num = []

    def insert(self, val: int) -> bool:
        if val in self.pos:
            return False
        else:
            self.pos[val] = len(self.num)
            self.num.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.pos:
            return False
        else:
            self.num[self.pos[val]] = self.num[-1]
            self.pos[self.num[-1]] = self.pos[val]
            self.num.pop()
            self.pos.pop(val)
            return True

    def getRandom(self) -> int:
        return random.choice(self.num)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()