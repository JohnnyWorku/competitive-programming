# Problem: Restore IP Addresses - https://leetcode.com/problems/restore-ip-addresses/

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12:
            return []

        res = []
        def backtrack(index=0, no_dots=0, curr_ip=""):
            if no_dots == 4 and index == len(s):
                res.append(curr_ip[:-1])
                return

            if no_dots > 4:
                return

            for i in range(index, min(len(s), index + 3)):
                if int(s[index: i + 1]) < 256 and (index == i or s[index] != "0"):
                    backtrack(i + 1, no_dots + 1, curr_ip + s[index : i + 1] + ".")

        backtrack()
        return res
        