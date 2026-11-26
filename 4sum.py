# 18. 4Sum (Medium)
# https://leetcode.com/problems/4sum/

# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#
# 	- 0 <= a, b, c, d < n
# 	- a, b, c, and d are distinct.
# 	- nums[a] + nums[b] + nums[c] + nums[d] == target
#
# You may return the answer in any order.
#
#
# Example 1:
#
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#
# Example 2:
#
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]
#
#
# Constraints:
#
# 	- 1 <= nums.length <= 200
# 	- -10^9 <= nums[i] <= 10^9
# 	- -10^9 <= target <= 10^9


# BRUTE FORCE APPROACH
# try every combination of 4 indices, sort each quad and put it in a set
# so duplicates get removed
# TC: O(n^4), SC: O(no. of unique quads)

def fourSumBrute(nums, target):
    n = len(nums)
    res = set()
    for a in range(n):
        for b in range(a + 1, n):
            for c in range(b + 1, n):
                for d in range(c + 1, n):
                    if nums[a] + nums[b] + nums[c] + nums[d] == target:
                        res.add(tuple(sorted([nums[a], nums[b], nums[c], nums[d]])))
    return [list(q) for q in res]


# OPTIMAL APPROACH
# sort the array, fix first two numbers with 2 loops, then use two pointers
# for the last two (same idea as 3sum, just one extra loop)
# skip same values at every level to avoid duplicate quads
# TC: O(n^3), SC: O(1) apart from the output

def fourSum(nums, target):
    nums.sort()
    n = len(nums)
    res = []
    for i in range(n - 3):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, n - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            left, right = j + 1, n - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    res.append([nums[i], nums[j], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < target:
                    left += 1
                else:
                    right -= 1
    return res


print(sorted(fourSumBrute([1, 0, -1, 0, -2, 2], 0)))  # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(fourSumBrute([2, 2, 2, 2, 2], 8))  # [[2,2,2,2]]
print(fourSum([1, 0, -1, 0, -2, 2], 0))  # [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
print(fourSum([2, 2, 2, 2, 2], 8))  # [[2,2,2,2]]
