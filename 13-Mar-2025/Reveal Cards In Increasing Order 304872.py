# Problem: Reveal Cards In Increasing Order - https://leetcode.com/problems/reveal-cards-in-increasing-order/

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        # # Doing the reverse way(from last to the first)
        # deck.sort()

        # res = deque()
        # for i in range(len(deck) - 1, -1, -1):
        #     if res:
        #         last = res.pop()
        #         res.appendleft(last)
        #     res.appendleft(deck[i])

        # return list(res)

        # Doing forward way
        deck.sort()

        res = [0]  * len(deck)
        indice_queue = deque(range(len(deck)))

        for card in deck:
            index = indice_queue.popleft()
            res[index] = card

            if indice_queue:
                to_be_placed_at_back = indice_queue.popleft()
                indice_queue.append(to_be_placed_at_back)

        return res
        