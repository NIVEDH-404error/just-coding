class Solution:
    def isValid(self, s: str) -> bool:
        hashmap={")":"(","}":"{","]":"["}
        stack=[]
        for c in s:
            if c not in hashmap:
                stack.append(c)
            else:
                if not stack:
                    return False #too many closing brackets
                else:
                    popped=stack.pop()
                    if popped!=hashmap[c]:
                        return False
        if not stack:
            return True
        else:
            return False