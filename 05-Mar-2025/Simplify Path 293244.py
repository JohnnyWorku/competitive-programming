# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        output = []
        curr_path = ""

        for char in path + "/":
            if char == "/":
                if output and curr_path == "..":
                    output.pop()
                elif curr_path and curr_path != "." and curr_path != "/" and curr_path != "..":
                    output.append(curr_path)

                curr_path = ""
            else:
                curr_path += char

        return "/" + "/".join(output)

        