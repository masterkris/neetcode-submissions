class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # DP array
        # spot in DP array -> DP[i] = s up to i can be segmented
        # dp[0] = True
        # from any i where dp is true, set dp[i + len(word)] = True if the substring from i to i + len(word) equals that word in the string
        # time: O(n * m * l) -> n is length str, m is length of dict, l is avg. length of str
        # space: O(n)

        dp = [False] * (len(s) + 1)
        dp[0] = True

        for i in range(len(s)):
            if not dp[i]:
                continue
                
            for word in wordDict:
                if i + len(word) <= len(s):
                    if s[i:i+len(word)] == word:
                        dp[i + len(word)] = True
        
        return dp[len(s)]

        