# 1. 两数之和
# 方法一：两层循环，O(n²)
class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# 方法二：字典，O(n)
# 思路：边走边记。先查需要的数出现过没有，没有就把当前数记下
# class Solution:
#     def twoSum(self,nums:List[int],target:int)->List[int]:
#         seen={}
#         for i in range(len(nums)):
#             need=target-nums[i]
#             if need in seen:
#                 return [seen[need],i]
#             seen[nums[i]]=i