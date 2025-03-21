# Problem: E - Minimum Subsequence - https://codeforces.com/gym/594077/problem/E

# The idea is trying to simulate the whole subsequence creating process using dictionaries
from collections import defaultdict,deque

for _ in range(int(input())):
    n = int(input())
    s = input()
    
    last_char_nos = defaultdict(int)
    sub_sequences_endings = defaultdict(deque)
    sub_sequence_no = 0
    their_sub_sequence = []
    
    for binary in s:
        if binary == "0" and last_char_nos["1"] > 0:
            last_char_nos["0"] += 1
            last_char_nos["1"] -= 1
            their_sub_sequence.append(sub_sequences_endings["1"][0])
            sub_sequences_endings["0"].append(sub_sequences_endings["1"][0])
            sub_sequences_endings["1"].popleft()
        elif binary == "1" and last_char_nos["0"] > 0:
            last_char_nos["1"] += 1
            last_char_nos["0"] -= 1
            their_sub_sequence.append(sub_sequences_endings["0"][0])
            sub_sequences_endings["1"].append(sub_sequences_endings["0"][0])
            sub_sequences_endings["0"].popleft()
        else:
            last_char_nos[binary] += 1
            sub_sequence_no += 1
            sub_sequences_endings[binary].append(sub_sequence_no)
            their_sub_sequence.append(sub_sequence_no)
            
    print(sub_sequence_no)
    print(*their_sub_sequence)
            