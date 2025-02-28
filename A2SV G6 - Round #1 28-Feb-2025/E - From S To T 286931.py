# Problem: E - From S To T - https://codeforces.com/gym/585107/problem/E

from collections import Counter

for _ in range(int(input())):
    s = input()
    t = input()
    p = input()
    
    if len(s) > len(t):
        print("NO")
    else:
        p_counter = Counter(p)
        s_pointer = 0
        t_pointer = 0
        
        can_be_equal = True
        while t_pointer < len(t):
            if s[s_pointer] == t[t_pointer]:
                s_pointer += 1
                t_pointer += 1
            else:
                if p_counter.get(t[t_pointer], 0) > 0:
                    p_counter[t[t_pointer]] -= 1
                    t_pointer += 1
                else:
                    can_be_equal = False
                    break
                
            if s_pointer >= len(s):
                while t_pointer < len(t):
                    if p_counter.get(t[t_pointer], 0) > 0:
                        p_counter[t[t_pointer]] -= 1
                        t_pointer += 1
                    else:
                        can_be_equal = False
                        break
                    
            if not can_be_equal:
                break
            
        if can_be_equal:
            print("YES")
        else:
            print("NO")