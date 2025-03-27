# Problem:  Insert into a Binary Search Tree - https://leetcode.com/problems/insert-into-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)

        if not root:
            return new_node

        def insert(curr_node, prev_node, new_node):
            if not curr_node:
                if prev_node.val > new_node.val:
                    prev_node.left = new_node
                else:
                    prev_node.right = new_node
                return

            if curr_node.val > new_node.val:
                prev_node = curr_node
                insert(curr_node.left, prev_node, new_node)
            else:
                prev_node = curr_node
                insert(curr_node.right, prev_node, new_node)

        insert(root, None, new_node)

        return root
        