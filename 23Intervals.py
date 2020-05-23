class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        intervalCommonList = []        
        i = 0
        j=0
        while i<len(A) and j<len(B):
            newitem = []
            if A[i][0] > B[j][1]:
                j+=1
                continue
            elif A[i][1] < B[j][0]:
                i+=1
                continue
            newitem = [max(A[i][0],B[j][0]), min(A[i][1], B[j][1])]
            if(B[j][1]>A[i][1]):
                i+=1
            else:
                j+=1
            intervalCommonList.append(newitem)
            
        return intervalCommonList
