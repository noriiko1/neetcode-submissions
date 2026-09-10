class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 # creates the two pointers
        
        while l <= r: # iteration of the array so left isnt crossed from r
            m = l + ((r - l) // 2) # middle = left + half the current size

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1
        