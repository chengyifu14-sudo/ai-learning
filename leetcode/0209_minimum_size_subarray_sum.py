class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        left=0
        windows=0
        best=float("inf")
        for right in range(len(nums)):
            windows+=nums[right]
            while windows >=target:
                windows-=nums[left]
                best=min(best,right-left +1)
                left+=1
        if best==float("inf"):
            return 0
        return best