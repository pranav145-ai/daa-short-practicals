# Experiment 4: Binary Search
# Aim: Find a target in a sorted list.
# Algorithm: Check middle; discard half that cannot contain target; repeat.
# Pseudocode: low=0, high=n-1; compare middle and adjust bounds until found or empty.
# Flowchart: Start -> check mid -> found? output; else halve range -> repeat.
# Sample: numbers 2 8 5 1 9, target 8 -> index 3 after sorting.
# Complexity: O(log n) time, O(1) extra space. Input must be sorted.
# Viva: Why log n? The search interval halves each step.
def binary(a, x):
    lo, hi = 0, len(a)-1
    while lo <= hi:
        mid = (lo+hi)//2
        if a[mid] == x: return mid
        if a[mid] < x: lo = mid+1
        else: hi = mid-1
    return -1
a = sorted(map(int, input("Numbers: ").split()))
x = int(input("Target: "))
print("Sorted list:", a)
print("Index:", binary(a, x))