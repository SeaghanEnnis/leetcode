class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        found = [False] * (len(s) + 1)
        found[len(s)] = True
        
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if(i + len(w)) <= len(s) and s[i : s + len(w)] == w:
                    found[i] = found[i + len(w)]
                if found[i]:
                    break


        return found[0]