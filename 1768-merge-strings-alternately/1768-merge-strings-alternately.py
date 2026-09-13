class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = []

        for i in range(min(len(word1), len(word2))):
            a.append(word1[i] + word2[i])

        r = "".join(a)

        if len(word1) > len(word2):
            return r + word1[min(len(word1), len(word2)):]
        else:
            return r + word2[min(len(word1), len(word2)):]