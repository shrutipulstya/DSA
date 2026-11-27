# 3965. Finish Time of Tasks I (Medium)
# https://leetcode.com/problems/finish-time-of-tasks-i/

# You are given an integer n representing the number of tasks in a project, numbered from 0 to n - 1. These tasks are connected as a tree rooted at task 0. This is represented by a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that task ui is the parent of task vi.
#
# You are also given an array baseTime of length n, where baseTime[i] represents the time to complete task i.
#
# The finish time of each task is calculated as follows:
#
# 	- Leaf task: The finish time is baseTime[i].
# 	- Non-leaf task:
#
# 		- Let earliest be the minimum finish time among its children, and latest be the maximum finish time among its children.
# 		- Let ownDuration be (latest - earliest) + baseTime[i].
# 		- The finish time of task i is latest + ownDuration.
#
#
#
# Return the finish time of the root task 0.
#
#
# Example 1:
#
# Input: n = 3, edges = [[0,1],[1,2]], baseTime = [9,5,3]
#
# Output: 17
#
# Explanation:
#      0 9  1 5  2 3
#
# 	- Task 2 is a leaf, so its finish time is baseTime[2] = 3.
# 	- Task 1 has one child task 2:
#
# 		- earliest = latest = 3
# 		- ownDuration = (latest - earliest) + baseTime[1] = 5
# 		- Finish time of task 1 is 3 + 5 = 8
#
#
# 	- Task 0 has one child with finish time 8:
#
# 		- earliest = latest = 8
# 		- ownDuration = (latest - earliest) + baseTime[0] = 9
# 		- Finish time of task 0 is 8 + 9 = 17
#
#
#
# Example 2:
#
# Input: n = 3, edges = [[0,1],[0,2]], baseTime = [4,7,6]
#
# Output: 12
#
# Explanation:
#      0 4  1 7  2 6
#
# 	- Task 1 is a leaf, so its finish time is baseTime[1] = 7.
# 	- Task 2 is a leaf, so its finish time is baseTime[2] = 6.
# 	- Task 0 has two children with finish times 7 and 6:
#
# 		- earliest = 6, latest = 7
# 		- ownDuration = (latest - earliest) + baseTime[0] = (7 - 6) + 4 = 5
# 		- Finish time of task 0 is latest + ownDuration = 7 + 5 = 12
#
#
#
# Example 3:
#
# Input: n = 4, edges = [[0,1],[0,2],[2,3]], baseTime = [5,8,2,1]
#
# Output: 18
#
# Explanation:
#
# 	- Task 1 is a leaf, so its finish time is baseTime[1] = 8.
# 	- Task 3 is a leaf, so its finish time is baseTime[3] = 1.
# 	- Task 2 has one child task 3:
#
# 		- earliest = latest = 1
# 		- ownDuration = (latest - earliest) + baseTime[2] = 0 + 2 = 2
# 		- Finish time of task 2 is latest + ownDuration = 1 + 2 = 3
#
#
# 	- Task 0 has two children with finish times 8 and 3:
#
# 		- earliest = 3, latest = 8
# 		- ownDuration = (latest - earliest) + baseTime[0] = (8 - 3) + 5 = 10
# 		- Finish time of task 0 is latest + ownDuration = 8 + 10 = 18
#
#
#
#
# Constraints:
#
# 	- 1 <= n <= 10^5
# 	- edges.length = n - 1
# 	- edges[i] == [ui, vi]
# 	- 0 <= ui, vi <= n - 1
# 	- ui != vi
# 	- The input is generated such that edges represents a valid tree.
# 	- baseTime.length == n
# 	- 1 <= baseTime[i] <= 10^5​​​​​​​
# 	- The finish time of every task is guaranteed to be less than 2^53.


# BRUTE FORCE APPROACH
# a task can be finished only once all its children are finished
# so keep scanning all tasks again and again, and compute finish time for any
# task whose children are all done. stop when root (0) is done
# TC: O(n^2) in worst case (like a long chain), SC: O(n)

def finishTimeBrute(n, edges, baseTime):
    children = [[] for _ in range(n)]
    for u, v in edges:
        children[u].append(v)

    finish = [None] * n
    while finish[0] is None:
        for i in range(n):
            if finish[i] is not None:
                continue
            if all(finish[c] is not None for c in children[i]):
                if not children[i]:
                    finish[i] = baseTime[i]
                else:
                    times = [finish[c] for c in children[i]]
                    latest, earliest = max(times), min(times)
                    finish[i] = latest + (latest - earliest) + baseTime[i]
    return finish[0]


# OPTIMAL APPROACH
# finish time of a task depends only on its children -> post order traversal
# do a bfs from root to get an order where every parent comes before its child
# then go through it in reverse so children are always processed first
# (not using recursive dfs because n can be 1e5 -> python recursion limit)
# TC: O(n), SC: O(n)

def finishTime(n, edges, baseTime):
    children = [[] for _ in range(n)]
    for u, v in edges:
        children[u].append(v)

    order = [0]
    for node in order:
        order.extend(children[node])

    finish = [0] * n
    for node in reversed(order):
        if not children[node]:
            finish[node] = baseTime[node]
        else:
            latest = max(finish[c] for c in children[node])
            earliest = min(finish[c] for c in children[node])
            finish[node] = latest + (latest - earliest) + baseTime[node]
    return finish[0]


print(finishTimeBrute(3, [[0, 1], [1, 2]], [9, 5, 3]))  # 17
print(finishTimeBrute(3, [[0, 1], [0, 2]], [4, 7, 6]))  # 12
print(finishTimeBrute(4, [[0, 1], [0, 2], [2, 3]], [5, 8, 2, 1]))  # 18
print(finishTime(3, [[0, 1], [1, 2]], [9, 5, 3]))  # 17
print(finishTime(3, [[0, 1], [0, 2]], [4, 7, 6]))  # 12
print(finishTime(4, [[0, 1], [0, 2], [2, 3]], [5, 8, 2, 1]))  # 18
