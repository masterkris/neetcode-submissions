class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        # first differing char
        # if word A is prefix of word B, word B must be AFTER word A

        orderInd = {c: i for i, c in enumerate(order)} # character -> index key

        for i in range(len(words) - 1):
            word1, word2 = words[i], words[i+1]

            for j in range(len(word1)):
                if j == len(word2):
                    return False
            
                if word1[j] != word2[j]:
                    if orderInd[word2[j]] < orderInd[word1[j]]:
                        return False
                    break
        
        return True




        