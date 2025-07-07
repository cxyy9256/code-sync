class RandomizedSet(object):

    def __init__(self):
        self.val_to_idx = {} # key: val, val = idx, important for running in O(1)
        self.values = []

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
        self.val_to_idx[val] = len(self.values)
        self.values.append(val)
        return True
    
    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False
        idx_to_remove = self.val_to_idx[val]
        last_element = self.values[-1]

        self.values[idx_to_remove] = last_element
        self.val_to_idx[last_element] = idx_to_remove

        self.values.pop()
        del self.val_to_idx[val]

        return True

    def getRandom(self) -> int:
        return random.choice(self.values) 
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()