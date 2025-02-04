# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

class Solution:
    def maskPII(self, s: str) -> str:
        answer = ""

        if "@" in s:
            answer += s[0].lower() + "*****" + s[s.find("@") - 1].lower() + s[s.find("@"):].lower()
        
        else:
            for digit in s:
                if digit.isalnum():
                    answer += digit

            if len(answer) == 10:
                answer = "***-***-" + answer[-4:]
            elif len(answer) == 11:
                answer = "+*-***-***-" + answer[-4:]
            elif len(answer) == 12:
                answer = "+**-***-***-" + answer[-4:]
            else:
                answer = "+***-***-***-" + answer[-4:]

        return answer
