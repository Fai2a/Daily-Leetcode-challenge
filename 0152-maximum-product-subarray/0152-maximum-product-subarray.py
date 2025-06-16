class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        currMax = currMin = 1

        for n in nums:
            temp = n*currMax
            currMax = max(n*currMax, n*currMin, n) #[-1, 5]
            currMin = min(temp, n*currMin, n) #[0, -1, -20]
            res = max(res, currMax, currMin)
        return res