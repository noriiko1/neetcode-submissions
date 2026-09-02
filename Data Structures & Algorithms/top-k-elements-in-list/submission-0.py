class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        max = 0

        for num in nums:
            if num in numMap:
                numMap[num] += 1
            else:
                numMap[num] = 1

        arr = []
        for num, count in numMap.items():
            arr.append([count,num])
        arr.sort()

        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res


            
            