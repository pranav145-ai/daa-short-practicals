# Experiment 2: Insertion Sort
# Aim: Insert each item into its correct place in the sorted left part.
# Algorithm: Shift values larger than key right, then insert key.
# Pseudocode: For i=1..n-1, save key; shift larger previous values; place key.
# Flowchart: Start -> choose key -> shift larger values -> insert key -> next -> output.
# Sample: 9 5 1 4 3 -> [1, 3, 4, 5, 9]
# Complexity: Best O(n), average/worst O(n^2), space O(1).
# Viva: Useful for nearly sorted data; in-place; reverse order is worst case.
def insertion(a):
    for i in range(1, len(a)):
        key, j = a[i], i-1
        while j >= 0 and a[j] > key:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
    return a
a = list(map(int, input("Numbers: ").split()))
print("Sorted:", insertion(a))