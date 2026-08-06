class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for ans in nums:
            ans = nums + nums
        return ans
        