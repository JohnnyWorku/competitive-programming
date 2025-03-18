# Problem: Binary Tree Preorder Traversal - https://leetcode.com/problems/binary-tree-preorder-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traverse_helper(node):
            if not node:
                return

            res.append(node.val)
            traverse_helper(node.left)
            traverse_helper(node.right)
            
        traverse_helper(root)
        return res
        