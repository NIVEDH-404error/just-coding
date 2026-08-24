class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for i in nums:
            if i not in seen:
                seen.add(i)
            else:
                return True
        return False
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        seen=set()
        for number in nums:
            if number in seen:
                return True
            else:
                seen.add(number)
        return False




        '''