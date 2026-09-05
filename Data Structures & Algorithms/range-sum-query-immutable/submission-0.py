class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        self.total = 0

        for n in range(len(nums)):
            self.total += nums[n]
            self.prefix.append(self.total)

    def sumRange(self, left: int, right: int) -> int:
        preRight = self.prefix[right]
        preLeft = self.prefix[left - 1] if left > 0 else 0
        return preRight - preLeft



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)