class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        totalMaxLength = 0
        currentMaxLength = 0
        n =0
        numsDict = {}
        numsDict[0] = -1
        for i in range(0, len(nums)):
            if nums[i] == 1:
                n +=1
            else:
                n-=1
            if n not in numsDict:
                numsDict[n] = i
            else:
                currentMaxLength = i - numsDict[n] 
                totalMaxLength = max(totalMaxLength, currentMaxLength)
        return totalMaxLength
                
