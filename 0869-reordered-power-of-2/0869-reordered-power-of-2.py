class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        sorted_n = ''.join(sorted(str(n)))

        for i in range(31):            
            power = 1 << i 
            if sorted_n == ''.join(sorted(str(power))):
                return True

        return False