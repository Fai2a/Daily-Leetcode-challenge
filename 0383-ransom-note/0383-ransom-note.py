class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for i in magazine:
            if (i not in dic):
                dic[i] = 1
            else:
                dic[i] += 1
        for i in ransomNote:
            if (i in dic and dic[i] > 0):
                dic[i] -= 1
            else:
                return False

        return True