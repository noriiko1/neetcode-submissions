class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        
        if zero_count > 1:
            return [0] * len(nums)
        
        if zero_count == 1:
            prod = 1
            for x in nums:
                if x != 0:
                    prod *= x
            return [prod if x == 0 else 0 for x in nums]

        total = nums[0]
        for n in range(1, len(nums)):
            total *= nums[n]
        
        for i in range(len(nums)):
            nums[i] = total // nums[i]

        return nums