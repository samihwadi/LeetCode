# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # DFS since summing values from root-to-leaf
        def dfs(root_node, cur):
            if not root_node:
                return 0
            # Shifts previous number to the left
            cur = cur * 10 + root_node.val
            if root_node.left is None and root_node.right is None:
                return cur
            return dfs(root_node.left, cur) + dfs(root_node.right, cur)
        return dfs(root, 0)

                

        