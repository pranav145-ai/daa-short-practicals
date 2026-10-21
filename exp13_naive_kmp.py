# Experiment 13: Naive and KMP String Matching
# Aim: Find pattern positions using naive matching and KMP.
# Algorithm: Naive checks each shift; KMP uses LPS to avoid redundant comparisons.
# Pseudocode: Build LPS; scan text; on mismatch shift pattern index using LPS.
# Flowchart: Start -> build LPS -> compare -> report match or shift -> continue.
# Sample text ababcabc, pattern abc -> [2,5].
# Complexity: Naive O(n*m); KMP O(n+m); KMP extra space O(m).
# Viva: LPS is the longest proper prefix also a suffix.
def naive(t,p):
 return [i for i in range(len(t)-len(p)+1) if t[i:i+len(p)]==p]
def kmp(t,p):
 if not p: return list(range(len(t)+1))
 lps=[0]*len(p); j=0
 for i in range(1,len(p)):
  while j and p[i]!=p[j]: j=lps[j-1]
  if p[i]==p[j]: j+=1; lps[i]=j
 i=j=0; ans=[]
 while i<len(t):
  if t[i]==p[j]: i+=1; j+=1
  if j==len(p): ans.append(i-j); j=lps[j-1]
  elif i<len(t) and t[i]!=p[j]:
   if j: j=lps[j-1]
   else: i+=1
 return ans
t,p=input('Text: '),input('Pattern: ')
print('Naive:',naive(t,p),'KMP:',kmp(t,p))