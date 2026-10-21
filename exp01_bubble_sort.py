# Experiment 1: Bubble Sort
# Aim: Sort a list using adjacent comparisons and swaps.
# Algorithm: Compare neighbours, swap if out of order; stop if a pass makes no swaps.
# Pseudocode: For each pass, compare adjacent items; swap if needed; early-exit if unchanged.
# Flowchart: Start -> compare/swap pass -> any swaps? -> repeat or print sorted list.
# Sample: 5 1 4 2 8 -> [1, 2, 4, 5, 8]
# Complexity: Best O(n), average/worst O(n^2), space O(1).
# Viva: Stable? Yes. Worst case? Reverse-sorted input.
def bubble(a):
    for i in range(len(a)-1):
        changed = False
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                changed = True
        if not changed: break
    return a
a = list(map(int, input("Numbers: ").split()))
print("Sorted:", bubble(a))