class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0                    # 从位置 0 开始放
        for i in range(len(nums)):  # i 是下标
            if nums[i] != 0:
                nums[slow]= nums[i]    # 把这个非零数放到哪里？
                slow+=1            # 放完以后 slow 怎么变？
        for j in range(slow, len(nums)):
            nums[j] = 0
