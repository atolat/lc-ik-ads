# 100. Same Tree
# Easy

# Given two binary trees, write a function to check if they are the same or not.

# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# Example 1:

# Input:     1         1
#           / \       / \
#          2   3     2   3

#         [1,2,3],   [1,2,3]

# Output: true
# Example 2:

# Input:     1         1
#           /           \
#          2             2

#         [1,2],     [1,null,2]

# Output: false
# Example 3:

# Input:     1         1
#           / \       / \
#          2   1     1   2

#         [1,2,1],   [1,1,2]

# Output: false

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # Edge Cases
        if not p and not q:
            return True
        elif not p or not q:
            return False

        queue = collections.deque()
        queue.append((p, q))

        while queue:
            numnodes = len(queue)
            for _ in range(numnodes):
                node_p, node_q = queue.popleft()
                if node_p.left and node_q.left:
                    queue.append((node_p.left, node_q.left))
                elif node_p.left or node_q.left:
                    return False
                if node_p.right and node_q.right:
                    queue.append((node_p.right, node_q.right))
                elif node_p.right or node_q.right:
                    return False
                if node_p.val != node_q.val:
                    return False
        return True
