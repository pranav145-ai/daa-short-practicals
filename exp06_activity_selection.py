# Experiment 6: Activity Selection (Greedy)
# Aim: Select the maximum number of non-overlapping activities.
# Algorithm: Sort by finish time; take each activity whose start >= last selected finish.
# Pseudocode: Sort by end; select first; scan and select compatible activities.
# Flowchart: Start -> sort by finish -> compatible? select -> scan next -> output.
# Sample activities below -> [(1, 3), (4, 6), (6, 7), (8, 9)]
# Complexity: O(n log n) including sorting; O(n) if pre-sorted.
# Viva: Greedy choice is earliest finish time; goal is maximum compatible activities.
activities = [(1, 3), (2, 5), (4, 6), (6, 7), (5, 9), (8, 9)]
activities.sort(key=lambda x: x[1])
chosen, finish = [], -1
for start, end in activities:
    if start >= finish:
        chosen.append((start, end))
        finish = end
print("Selected:", chosen)