class Solution:
    def numDecodings(self, s: str) -> int:

        # dp[i] = num. ways to decode substring starting at index i
        # i = 0 --> 226
        # i = 1 --> 26
        # i = 2 --> 6
        # i = 3 --> empty string
        # can either take one digit OR two digits at each position
        # dp[i], dp[i+1], dp[i+2]
        # trace 1012
        # dp[i] = dp[i + 1] + dp[i + 2]

        dp = {len(s) : 1}   # string itself has one valid decoding

        for i in range(len(s) - 1, -1, -1):

            if s[i] == "0":   
                dp[i] = 0
            else:
                dp[i] = dp[i + 1] 
                # decode one digit, how many ways remain is number of ways to decode rest

            # take 2 digits together
            # do we have 2 digits? up to 26
            if i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                dp[i] += dp[i + 2]
        
        return dp[0]






        