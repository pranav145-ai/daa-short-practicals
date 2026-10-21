# Experiment 15: Vertex Cover Approximation
# Aim: Find an approximate vertex cover of an undirected graph.
# Algorithm: Pick an uncovered edge; add both endpoints; remove edges incident to either endpoint.
# Pseudocode: While edges remain, choose (u,v), add u,v, discard incident edges.
# Flowchart: Start -> choose edge -> add endpoints -> remove incident edges -> repeat.
# Sample edges are provided; valid cover may depend on edge order.
# Complexity: O(E^2) worst-case for this simple edge-filtering version; O(V+E) space.
# Viva: Vertex cover touches every edge; standard edge-picking algorithm is a 2-approximation.
def vertex_cover(edges):
 edges=set(tuple(sorted(e)) for e in edges)
 cover=set()
 while edges:
  u,v=next(iter(edges))
  cover.update((u,v))
  edges={e for e in edges if u not in e and v not in e}
 return sorted(cover)
edges=[(1,2),(2,3),(3,4),(4,1),(2,4)]
print('Approximate cover:',vertex_cover(edges))