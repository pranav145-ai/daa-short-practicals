# Experiment 7: Huffman Coding
# Aim: Generate variable-length prefix codes from symbol frequencies.
# Algorithm: Repeatedly combine two minimum-frequency nodes; left edge=0, right edge=1.
# Pseudocode: Put leaves in min-heap; combine two minima until one tree remains; traverse.
# Flowchart: Start -> min-heap -> combine two minima -> one node? -> print codes.
# Sample frequencies: a5 b9 c12 d13 e16 f45; code choices may vary with ties.
# Complexity: O(k log k) time and O(k) space for k symbols.
# Viva: Prefix-free means no code is prefix of another; frequent symbols get shorter codes.
import heapq
freq = {"a": 5, "b": 9, "c": 12, "d": 13, "e": 16, "f": 45}
heap = [[w, [ch, ""]] for ch, w in freq.items()]
heapq.heapify(heap)
while len(heap) > 1:
    lo, hi = heapq.heappop(heap), heapq.heappop(heap)
    for pair in lo[1:]: pair[1] = "0" + pair[1]
    for pair in hi[1:]: pair[1] = "1" + pair[1]
    heapq.heappush(heap, [lo[0]+hi[0]] + lo[1:] + hi[1:])
for ch, code in sorted(heap[0][1:], key=lambda p: p[0]):
    print(ch, code)