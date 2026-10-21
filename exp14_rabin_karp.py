# Experiment 14: Rabin-Karp
# Aim: Find pattern occurrences using rolling hashes.
# Algorithm: Hash pattern and each text window; verify characters when hashes match.
# Pseudocode: Initialize hashes; compare each window; roll hash by removing old and adding new char.
# Flowchart: Start -> calculate hashes -> compare -> slide window -> print positions.
# Sample abracadabra / abra -> [0,7].
# Complexity: Average O(n+m), worst O(n*m) due to collisions.
def rabin_karp(t,p,base=256,mod=101):
 n,m=len(t),len(p)
 if m==0: return list(range(n+1))
 if m>n: return []
 h=pow(base,m-1,mod); ph=th=0; ans=[]
 for i in range(m):
  ph=(base*ph+ord(p[i]))%mod
  th=(base*th+ord(t[i]))%mod
 for i in range(n-m+1):
  if ph==th and t[i:i+m]==p: ans.append(i)
  if i<n-m: th=(base*(th-ord(t[i])*h)+ord(t[i+m]))%mod
 return ans
print('Matches:',rabin_karp(input('Text: '),input('Pattern: ')))