class RandomizedSet:

    def __init__(self):
        self.numMap = {}
        self.nums = []
        
    def insert(self, val: int) -> bool:
        if val in self.numMap:
            return False
        self.numMap[val] = len(self.nums) 
        self.nums.append(val)
        return True      

    def remove(self, val: int) -> bool:
        if val not in self.numMap:
            return False
        idx_to_remove = self.numMap[val]
        last_val = self.nums[-1]

        self.nums[idx_to_remove] = last_val
        self.numMap[last_val] = idx_to_remove

        self.nums.pop()
        del self.numMap[val]

        return True
        

    def getRandom(self) -> int:
        return random.choice(self.nums)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()