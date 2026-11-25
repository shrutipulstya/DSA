# 2937. Make Three Strings Equal (Easy)
# https://leetcode.com/problems/make-three-strings-equal/

# You are given three strings: s1, s2, and s3. In one operation you can choose one of these strings and delete its rightmost character. Note that you cannot completely empty a string.
#
# Return the minimum number of operations required to make the strings equal. If it is impossible to make them equal, return -1.
#
#
# Example 1:
#
# Input: s1 = "abc", s2 = "abb", s3 = "ab"
#
# Output: 2
#
# Explanation: Deleting the rightmost character from both s1 and s2 will result in three equal strings.
#
# Example 2:
#
# Input: s1 = "dac", s2 = "bac", s3 = "cac"
#
# Output: -1
#
# Explanation: Since the first letters of s1 and s2 differ, they cannot be made equal.
#
#
# Constraints:
#
# 	- 1 <= s1.length, s2.length, s3.length <= 100
# 	- s1, s2 and s3 consist only of lowercase English letters.


# BRUTE FORCE APPROACH
# keep deleting the last char of the longest string until all three are equal
# if any string would become empty, it's impossible
# TC: O(n^2) because of string slicing + comparing, SC: O(n)

def findMinimumOperationsBrute(s1, s2, s3):
    ops = 0
    while not (s1 == s2 == s3):
        longest = max(len(s1), len(s2), len(s3))
        if longest == 1:
            return -1
        if len(s1) == longest:
            s1 = s1[:-1]
        elif len(s2) == longest:
            s2 = s2[:-1]
        else:
            s3 = s3[:-1]
        ops += 1
    return ops


# OPTIMAL APPROACH
# we can only delete from the right, so whatever is left at the end has to be a
# common prefix of all three. find the longest common prefix (lcp)
# if lcp is 0 -> first chars differ -> -1
# else every extra char beyond lcp has to be deleted -> total len - 3 * lcp
# TC: O(n), SC: O(1)

def findMinimumOperations(s1, s2, s3):
    lcp = 0
    while lcp < min(len(s1), len(s2), len(s3)) and s1[lcp] == s2[lcp] == s3[lcp]:
        lcp += 1
    if lcp == 0:
        return -1
    return len(s1) + len(s2) + len(s3) - 3 * lcp


print(findMinimumOperationsBrute("abc", "abb", "ab"))  # 2
print(findMinimumOperationsBrute("dac", "bac", "cac"))  # -1
print(findMinimumOperations("abc", "abb", "ab"))  # 2
print(findMinimumOperations("dac", "bac", "cac"))  # -1
