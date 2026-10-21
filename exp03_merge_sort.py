# Experiment 3: Merge Sort
# Aim: Sort using divide and conquer.
# Algorithm: Split in halves, recursively sort, then merge in order.
# Pseudocode: If size<=1 return; sort halves; merge smallest remaining values.
# Flowchart: Start -> split -> sort halves -> merge -> output.
# Sample: 38 27 43 3 9 82 10 -> [3, 9, 10, 27, 38, 43, 82]
# Complexity: O(n log n) time, O(n) extra space.
# Viva: Paradigm? Divide and conquer. Stable? Yes. Drawback? Extra memory.
def merge_sort(a):
    if len(a) < 2: return a
    m = len(a)//2
    left, right = merge_sort(a[:m]), merge_sort(a[m:])
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: out.append(left[i]); i += 1
        else: out.append(right[j]); j += 1
    return out + left[i:] + right[j:]
a = list(map(int, input("Numbers: ").split()))
print("Sorted:", merge_sort(a))