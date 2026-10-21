# Experiment 8: Matrix Chain Multiplication (DP)
# Aim: Minimize scalar multiplications for a matrix chain.
# Algorithm: For each interval, try all split points and retain the least cost.
# Pseudocode: dp[i][j]=min(dp[i][k]+dp[k+1][j]+p[i]*p[k+1]*p[j+1]).
# Flowchart: Start -> initialize DP -> try splits -> save minimum -> print answer.
# Sample dimensions [10,30,5,60] -> 4500.
# Complexity: O(n^3) time, O(n^2) space. Viva: DP uses overlapping subproblems.
def matrix_chain(p):
    n=len(p)-1
    dp=[[0]*n for _ in range(n)]
    for L in range(2,n+1):
        for i in range(n-L+1):
            j=i+L-1
            dp[i][j]=min(dp[i][k]+dp[k+1][j]+p[i]*p[k+1]*p[j+1] for k in range(i,j))
    return dp[0][n-1]
print('Minimum multiplications:', matrix_chain([10,30,5,60]))