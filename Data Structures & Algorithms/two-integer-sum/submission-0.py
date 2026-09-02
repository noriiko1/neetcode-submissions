class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sumMap = {}

        for index, num in enumerate(nums):
            diff = target - num
            if diff in sumMap and index != sumMap[diff]:
                return sorted([index, sumMap[diff]])
            else:
                sumMap[num] = index