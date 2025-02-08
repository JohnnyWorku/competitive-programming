# Problem: Image Smoother - https://leetcode.com/problems/image-smoother/description/

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        rows = len(img)
        cols = len(img[0])

        ans = []

        for row in range(rows):
            row = []
            for col in range(cols):
               row.append(0)
            ans.append(row)

        for row in range(rows):
            for col in range(cols):
                
                total, count = 0, 0
                for r in range(row - 1, row + 2):
                    for c in range(col - 1, col + 2):
                        if (c < 0 or c == cols) or (r < 0 or r == rows):
                            continue
                        total += img[r][c]
                        count += 1

                ans[row][col] = total // count

        return ans
