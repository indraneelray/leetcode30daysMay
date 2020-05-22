# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left =1
        right =n
        
        while left<right:
            version = left + (right-left)/2
            if isBadVersion(version)==False:
                # bad version lies in the right half
                left = version +1
            else:
                # bad version lies in the first half
                right = version    
                
        return int(left)