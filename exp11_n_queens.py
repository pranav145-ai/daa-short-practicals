# Experiment 11: N-Queens (Backtracking)
# Aim: Place N queens without shared columns or diagonals.
# Algorithm: Try safe columns row by row; recursively explore each valid placement.
# Pseudocode: If row==N record solution; else try each safe column and recurse.
# Flowchart: Start -> try safe column -> next row -> solution? record; dead end? backtrack.
# Sample N=4 -> [1,3,0,2] and [2,0,3,1] (column per row).
# Complexity: Exponential, commonly bounded by O(N!); O(N) recursion state excluding results.
def queens(n,r=0,cols=None,pos=None,d1=None,d2=None):
 cols,pos=cols or set(),pos or []
 d1,d2=d1 or set(),d2 or set()
 if r==n: return [pos[:]]
 ans=[]
 for c in range(n):
  if c not in cols and r-c not in d1 and r+c not in d2:
   ans+=queens(n,r+1,cols|{c},pos+[c],d1|{r-c},d2|{r+c})
 return ans
for solution in queens(4): print(solution)