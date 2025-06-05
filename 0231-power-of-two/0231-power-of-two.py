class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # return n > 0 and (n&(n-1)) == 0

#2nd methord
        binary = bin(n).replace("0b","")
        if (n >= 0 and binary.count("1")) == 1:
            return True
        else:
            return False   