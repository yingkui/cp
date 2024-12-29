class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        m = n - numFriends + 1
        if numFriends == 1:
            return word
        return max(word[i:i + m] for i in range(n))

class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        n = len(word)
        if numFriends == 1:
            return word
            
        res = ""
        for i in range(n):
            j = min(i + n - numFriends, n-1)
            candidate = word[i:j+1]
            if candidate > res:
                res = candidate
        
        return res