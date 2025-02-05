# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        # file_dict = defaultdict(list)

        # for path in paths:
        #     dir_name, *files = path.split()

        #     for _file in files:
        #         f_name, f_content = _file.split("(")
        #         file_dict[f_content].append(f"{dir_name}/{f_name}")

        # ans = []
        # for f in file_dict.values():
        #     if len(f) > 1:   #to know whether duplicated or not
        #         ans.append(f)

        # return ans

        ans = []
        file_dict = defaultdict(list)

        for path in paths:
            dir_name, *files = path.split()

            for f in files:
                f_name, f_content = f.split("(")
                file_dict[f_content].append(f"{dir_name}/{f_name}")

        for _f in file_dict.values():
            if len(_f) > 1:
                ans.append(_f)

        return ans
        
