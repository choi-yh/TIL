class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False

        dic = defaultdict(int)
        for i in range(len(magazine)):
            dic[magazine[i]] += 1

        for i in range(len(ransomNote)):
            if dic.get(ransomNote[i], 0) == 0:
                return False
            
            dic[ransomNote[i]] -= 1

        return True
                
