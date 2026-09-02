class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxNum = -1  # Initialize maxNum to -1
        
        for i in range(len(arr) - 1, -1, -1):  # Iterate backwards through the list
            if arr[i] > maxNum:
                temp = arr[i]
                arr[i] = maxNum  # Replace current element with maxNum
                maxNum = temp  # Update maxNum to the previous value of arr[i]
            else:
                arr[i] = maxNum  # Replace current element with maxNum
        
        arr[-1] = -1  # Replace the last element with -1
        
        return arr