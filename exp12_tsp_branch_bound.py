# Experiment 12: Travelling Salesperson Problem
# Aim: Find a minimum-cost closed tour visiting each city once.
# This short reference enumerates tours; it is NOT full least-cost Branch and Bound.
# Algorithm: Fix city 0, enumerate remaining permutations, calculate cost, keep the cheapest.
# Pseudocode: For each permutation, form closed tour; update best if cost is lower.
# Flowchart: Start -> generate tour -> calculate cost -> improve best? -> next tour -> output.
# Sample matrix below -> minimum cost 80; 0-1-3-2-0 is one optimal tour.
# Complexity: O((n-1)!) time.
from itertools import permutations
cost=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
n=len(cost); best=(float('inf'),None)
for p in permutations(range(1,n)):
 tour=(0,)+p+(0,)
 total=sum(cost[tour[i]][tour[i+1]] for i in range(n))
 if total<best[0]: best=(total,tour)
print('Minimum cost:',best[0],'Tour:',best[1])