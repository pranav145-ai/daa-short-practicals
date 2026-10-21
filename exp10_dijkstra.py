# Experiment 10: Dijkstra's Shortest Path
# Aim: Find shortest distances from one source with non-negative edge weights.
# Algorithm: Min-heap selects closest vertex; relax outgoing edges.
# Pseudocode: dist[source]=0; pop minimum; update neighbours when a shorter path is found.
# Flowchart: Start -> initialize -> pop minimum -> relax -> heap empty? -> print distances.
# Sample graph below, source 0 -> {0:0, 1:3, 2:1, 3:4}.
# Complexity: O((V+E) log V) time, O(V+E) space. Negative edges are not supported.
import heapq
g={0:[(1,4),(2,1)],1:[(3,1)],2:[(1,2),(3,5)],3:[]}
dist={v:float('inf') for v in g}; dist[0]=0
heap=[(0,0)]
while heap:
 d,u=heapq.heappop(heap)
 if d!=dist[u]: continue
 for v,w in g[u]:
  if d+w<dist[v]:
   dist[v]=d+w
   heapq.heappush(heap,(dist[v],v))
print('Distances:',dist)