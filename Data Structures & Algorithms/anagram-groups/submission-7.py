class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        final = defaultdict(list)

        for s in strs:
            count = [0] * 26 # one for each letter in alphabet

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            final[tuple(count)].append(s) # create grouping

        return list(final.values())
        