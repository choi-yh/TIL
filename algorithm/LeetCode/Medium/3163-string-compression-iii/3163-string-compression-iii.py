class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""
        c = word[0]
        cnt = 0
        for i in range(len(word)):
            if word[i] != c or cnt == 9:
                comp += str(cnt) + c
                c = word[i]
                cnt = 1
            else:
                cnt += 1
        
        comp += str(cnt) + c
        return comp