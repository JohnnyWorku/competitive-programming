# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = []
        def in_order(curr_node):
            if not curr_node:
                return
            
            in_order(curr_node.left)
            res.append(curr_node.val)
            in_order(curr_node.right)

        def balanced_tree(arr):
            if not arr:
                return 

            mid = len(arr) // 2
            root = TreeNode(arr[mid])

            root.left = balanced_tree(arr[:mid])
            root.right = balanced_tree(arr[mid + 1:])

            return root

        in_order(root)

        return balanced_tree(res)
        