# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []

        for char in logs:
            if char == "../" and stack:
                stack.pop()
            elif char[:-1].isalnum(): # check the chars before "/" are alphanums
                stack.append(char)

        return len(stack)
        