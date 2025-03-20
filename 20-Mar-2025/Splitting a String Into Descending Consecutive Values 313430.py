# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
         
        def backtrack(path, index):
            if index == len(s):
                return len(path) >= 2  # At least two numbers must be present

            num = 0
            for i in range(index, len(s)):
                num = num * 10 + int(s[i])  # Forming the number
                
                # If there is a previous number, ensure the decreasing condition holds
                if not path or path[-1] - 1 == num:
                    path.append(num)
                    
                    if backtrack(path, i + 1):
                        return True
                    
                    path.pop()  # Backtrack

            return False

        return backtrack([], 0)
