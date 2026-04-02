class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        m, n = len(coins), len(coins[0])
        NEG = -10**18
        
        
        dp = [[[NEG] * n for _ in range(m)] for _ in range(3)]
        
    
        if coins[0][0] >= 0:
            dp[0][0][0] = coins[0][0]
        else:
            dp[0][0][0] = coins[0][0] 
            dp[1][0][0] = 0           
        
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                
                val = coins[i][j]
                
                for k in range(3):
                    
                    best_prev = NEG
                    if i > 0:
                        best_prev = max(best_prev, dp[k][i - 1][j])
                    if j > 0:
                        best_prev = max(best_prev, dp[k][i][j - 1])
                    
                    if best_prev != NEG:
                        dp[k][i][j] = max(dp[k][i][j], best_prev + val)
                    
                   
                    if val < 0 and k > 0:
                        best_prev_neutral = NEG
                        if i > 0:
                            best_prev_neutral = max(best_prev_neutral, dp[k - 1][i - 1][j])
                        if j > 0:
                            best_prev_neutral = max(best_prev_neutral, dp[k - 1][i][j - 1])
                        
                        if best_prev_neutral != NEG:
                            dp[k][i][j] = max(dp[k][i][j], best_prev_neutral)
        
        return max(dp[0][m - 1][n - 1], dp[1][m - 1][n - 1], dp[2][m - 1][n - 1])