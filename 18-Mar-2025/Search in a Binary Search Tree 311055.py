# Problem: Search in a Binary Search Tree - https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        res = None
        curr = root

        def helper(node):
            if not node:
                return
            if node.val == val:
                return node
            elif node.val < val:
                return helper(node.right)
            else:
                return helper(node.left)

        return helper(root)
        