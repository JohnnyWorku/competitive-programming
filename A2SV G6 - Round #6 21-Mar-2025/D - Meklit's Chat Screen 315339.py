# Problem: D - Meklit's Chat Screen - https://codeforces.com/gym/594077/problem/D

from collections import deque
n, k = map(int, input().split())
chat_ids = list(map(int, input().split()))

queue = deque()
queue_set = set()

for chat_id in chat_ids:
    if len(queue_set) < k and chat_id not in queue_set:
        queue_set.add(chat_id)
        queue.append(chat_id)
    elif len(queue_set) == k and chat_id not in queue_set:
        queue_set.remove(queue[0])
        queue.popleft()
        queue_set.add(chat_id)
        queue.append(chat_id)

queue.reverse()
print(len(queue))
print(*queue)

