class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        
        freqMap1 = dict.fromkeys(range(0,26), 0)
        
        for i,val in enumerate(s1):
            freqMap1[ord(val)-97] +=1
            
            
        
        freqWindow = dict.fromkeys(range(0,26), 0)
        
        for i,val in enumerate(s2):
            
            freqWindow[ord(val)-97] +=1 

            if i>=len(s1):
                left = s2[i-len(s1)]
                
                if freqWindow[ord(left)-97]==1:
                    freqWindow[ord(left)-97] =0
                else:
                    freqWindow[ord(left)-97]-=1

            if freqWindow == freqMap1:
                return True
            
        return False