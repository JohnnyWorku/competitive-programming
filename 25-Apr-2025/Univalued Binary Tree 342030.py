# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        # # BFS
        # value = root.val
        # queue = deque([root])

        # while queue:
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         if node.val != value:
        #             return False
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)

        # return True

        # DFS
        def dfs(node, value=root.val):
            if not node:
                return True

            if node.val != value:
                return False

            if not dfs(node.left) or not dfs(node.right):
                return False
            else:
                return True
 
            # return node.val == value and dfs(node.left) and dfs(node.right)

        return dfs(root)
        