class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i in s_hash:
                s_hash[i]=s_hash[i]+1
            else:
                s_hash[i]=1
        
        for char in t:
            if char in s_hash:
                s_hash[char]=s_hash[char]-1
            else:
                return False
        
        for key in s_hash:
            if s_hash[key]!=0:
                return False
            
        return True