# Experiment 5: Quick Sort
# Aim: Sort a list using pivot-based partitioning.
# Algorithm: Choose last item as pivot; partition smaller/equal left, larger right; recurse.
# Pseudocode: If size<2 return; split around pivot; sort both parts and join.
# Flowchart: Start -> choose pivot -> partition -> recursively sort -> combine.
# Sample: 7 2 9 4 1 -> [1, 2, 4, 7, 9]
# Complexity: Average O(n log n), worst O(n^2); simple version uses O(n) extra space.
# Viva: Worst case is unbalanced partitions. Paradigm: divide and conquer.
def quick(a):
    if len(a) < 2: return a
    p = a[-1]
    return quick([x for x in a[:-1] if x <= p]) + [p] + quick([x for x in a[:-1] if x > p])
a = list(map(int, input("Numbers: ").split()))
print("Sorted:", quick(a))