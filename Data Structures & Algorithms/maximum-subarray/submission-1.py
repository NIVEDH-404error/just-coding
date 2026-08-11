class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currentsum=nums[0]
        maxsum=nums[0]
        for i in range(1,len(nums)):
            currentsum=max(nums[i],currentsum+nums[i]) #2 #-1 #4 #2 #4 #5 #4 #8
            maxsum=max(maxsum,currentsum) #2 #2 #4 #4 #4 #5 #5 #8
        return maxsum

