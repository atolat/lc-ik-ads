# 276. Paint Fence
# Easy

# There is a fence with n posts, each post can be painted with one of the k colors.

# You have to paint all the posts such that no more than two adjacent fence posts have the same color.

# Return the total number of ways you can paint the fence.

# Note:
# n and k are non-negative integers.

# Example:

# Input: n = 3, k = 2
# Output: 6
# Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:

#             post1  post2  post3
#  -----      -----  -----  -----
#    1         c1     c1     c2
#    2         c1     c2     c1
#    3         c1     c2     c2
#    4         c2     c1     c1
#    5         c2     c1     c2
#    6         c2     c2     c1

class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0

        same = [0 for _ in range(n)]
        different = [0 for _ in range(n)]
        total = [0 for _ in range(n)]

        same[0] = 0
        different[0] = k
        total[0] = k

        for i in range(1, n):
            same[i] = different[i-1]
            different[i] = (k-1) * total[i-1]
            total[i] = same[i] + different[i]

        return total[-1]
