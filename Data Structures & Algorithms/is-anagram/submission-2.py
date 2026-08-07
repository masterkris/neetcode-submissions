class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # two hashmaps
        # if equal, True. else False.

        # length edge case
        if len(s) != len(t):
            return False

        s_map = {}
        t_map = {}

        # since same length
        for i in range(len(s)):
            s_map[s[i]] = 1 + s_map.get(s[i], 0)
            t_map[t[i]] = 1 + t_map.get(t[i], 0)
        
        return t_map == s_map
        