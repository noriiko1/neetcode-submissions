class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numCount = {}
        maxCount = 0
        maxValue = 0

        if len(nums) == 1:
            return nums[0]

        for i in range(len(nums)):
            if nums[i] in numCount:
                numCount[nums[i]] += 1
            else:
                numCount[nums[i]] = 0
        for i in range(len(numCount)):
            if numCount[nums[i]] > maxCount:
                maxValue = nums[i]
            maxCount = max(numCount[nums[i]], maxCount)
        return maxValue
        