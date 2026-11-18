class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        windows=sum(nums[:k])
        best=windows
        for i in range (k,len(nums)):
            windows=(windows+nums[i]-nums[i-k])
            best=max(best,windows)
        sol=best/k
        return sol
