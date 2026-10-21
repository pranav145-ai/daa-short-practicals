# Experiment 9: Longest Common Subsequence
# Aim: Find the longest common subsequence of two strings.
# Algorithm: DP table; equal characters extend diagonal, otherwise take max(top,left).
# Pseudocode: Fill table, then backtrack to reconstruct a longest sequence.
# Flowchart: Start -> fill DP table -> backtrack -> print result.
# Complexity: O(m*n) time and space.
def lcs(a,b):
 d=[[0]*(len(b)+1) for _ in range(len(a)+1)]
 for i in range(1,len(a)+1):
  for j in range(1,len(b)+1):
   if a[i-1]==b[j-1]: d[i][j]=d[i-1][j-1]+1
   else: d[i][j]=max(d[i-1][j],d[i][j-1])
 i,j,out=len(a),len(b),[]
 while i and j:
  if a[i-1]==b[j-1]: out.append(a[i-1]); i-=1; j-=1
  elif d[i-1][j]>=d[i][j-1]: i-=1
  else: j-=1
 return ''.join(reversed(out))
print('LCS:',lcs(input('First string: '),input('Second string: ')))