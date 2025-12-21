"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
"""


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # for each root you need to find which one of right or left is bigger and add it to the running total until you reach the tree root

        def max_len(root):
            if not root:
                return 0
            else:
                return 1 + max(max_len(root.left), max_len(root.right))

        return max_len(root)
