class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first_num=float("inf")
        second_num=float("inf")
        for i in nums:
            if i<=first_num:
                first_num=i
            elif i<=second_num:
                second_num=i
            else:
                return True
        return False            