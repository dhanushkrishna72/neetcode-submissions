class Solution:
    def canJump(self, nums: List[int]) -> bool:
        steps = 0

        for i in range(len(nums)):
            if i > steps:
                return False
            steps = max(steps,i + nums[i])

            if steps>len(nums):
                return True
            
        return True
                