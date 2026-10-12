class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # set prefix = strs[0]
        # start with 1 and go to end
        # if string doesn't have that prefix
        # try the same but with one char. less until we find that word

        # time: O(n * m^2) = n is num. strings and m. is max. string length
        # space : O(m)

        prefix = strs[0]

        for s in strs[1:]: 
            while not s.startswith(prefix):
                prefix = prefix[:-1]
        
        return prefix

        