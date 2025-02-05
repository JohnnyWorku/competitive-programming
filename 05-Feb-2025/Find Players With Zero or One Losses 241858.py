# Problem: Find Players With Zero or One Losses - https://leetcode.com/problems/find-players-with-zero-or-one-losses/

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_dict = defaultdict(int)
        zero_loss = []
        one_loss = []

        for match in matches:
            losser = match[1]
            loss_dict[losser] += 1
            
        for match in matches:
            if match[0] not in loss_dict and match[0] not in zero_loss:
                zero_loss.append(match[0])

        for key, value in loss_dict.items():
            if value == 1:
                one_loss.append(key)

        zero_loss.sort()
        one_loss.sort()

        return [zero_loss, one_loss]
