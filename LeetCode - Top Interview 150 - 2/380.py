class RandomizedSet:
    def __init__(self):
        self.values = []
        self.valueIndexMap = {}

    def insert(self, val: int) -> bool:
        if val in self.valueIndexMap:
            return False

        self.values.append(val)
        self.valueIndexMap[val] = len(self.values) - 1

        return True

    def remove(self, val: int) -> bool:
        if val not in self.valueIndexMap:
            return False

        target_index = self.valueIndexMap[val]
        last_value = self.values[-1]

        self.values[target_index] = last_value
        self.valueIndexMap[last_value] = target_index

        self.values.pop()
        del self.valueIndexMap[val]

        return True

    def getRandom(self) -> int:
        random_index = random.randint(0, len(self.values) - 1)

        return self.values[random_index]


"""
Edge Case

[0] Insert
[0] Remove
[0] GetRandom
[0] Insert
[0] Remove
[0] GetRandom
"""

"""
Every method in the solution uses a valIndexMap, empties the value at the index, and then takes the last element to put it in that spot. It feels like the approach is too focused on the 'clever idea' alone.
"""
