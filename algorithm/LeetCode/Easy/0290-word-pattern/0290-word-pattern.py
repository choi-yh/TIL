class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")

        if len(pattern) != len(words):
            return False

        pattern_check = dict()
        word_check = dict()

        for i in range(len(words)):
            p = pattern[i]
            word = words[i]

            if p not in pattern_check and word not in word_check:
                pattern_check[p] = word
                word_check[word] = p

            if p in pattern_check and pattern_check[p] != word:
                return False

            if word in word_check and word_check[word] != p:
                return False

        return True
