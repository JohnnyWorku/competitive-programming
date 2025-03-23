# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque([root] if root else [])
        res = []

        while queue:
            # res.append(max(queue, key= lambda node: node.val).val)
            row_max = queue[0].val
            for _ in range(len(queue)):
                node = queue.popleft()
                row_max = max(row_max, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(row_max)

        return res
