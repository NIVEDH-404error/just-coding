class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_mult=1
        r_mult=1
        n=len(nums)
        ans=[0]*n
        for i in range(n):
            ans[i]=l_mult
            l_mult*=nums[i]

        for i in range(n-1,-1,-1):
            ans[i]*=r_mult
            r_mult*=nums[i]
        return ans

    