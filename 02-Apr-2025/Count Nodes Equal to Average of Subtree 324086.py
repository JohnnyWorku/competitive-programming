# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        count = 0
        def post_order(curr_node):
            nonlocal count
            if not curr_node:
                return (0, 0)

            left_sum, left_count = post_order(curr_node.left)
            right_sum, right_count = post_order(curr_node.right)

            curr_sum = left_sum + right_sum + curr_node.val
            curr_count = left_count + right_count + 1

            curr_avg = curr_sum // curr_count

            if curr_avg == curr_node.val:
                count += 1

            return (curr_sum, curr_count)

        post_order(root)

        return count
        