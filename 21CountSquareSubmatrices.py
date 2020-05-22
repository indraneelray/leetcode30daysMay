class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        dp = [ [ 0 for i in range(0,len(matrix[0])+1) ] for j in range(0,len(matrix)+1) ]
        
        # for i in range(0, len(matrix)+1):
        #     for j in range(0, len(matrix[0])+1):
        #         dp[i][j]=0
        
        total = 0
        #print (dp)
        for i in range(1,len(matrix)+1):
            for j in range (1,len(matrix[0])+1):
                #print(matrix[i-1][j-1])
                if matrix[i-1][j-1]==0:
                    dp[i][j] =0
                else:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])+1
                total += dp[i][j]
                
        print (dp)
        return total