class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        #hashmap=value:index
        #nums=[1,2,3,4,9]
        #target=6
        for i,val in enumerate(nums):
            diff=target-val #6
            if diff in hashmap:
                return [hashmap[diff],i]

            else:
                hashmap[val]=i


        
                
