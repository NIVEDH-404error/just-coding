class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        #greedy approach sort
        hashmap={}
        for words in strs:
            sorted_word="".join(sorted(words))
            if sorted_word not in hashmap:
                hashmap[sorted_word]=[]
            hashmap[sorted_word].append(words)
        return list(hashmap.values())
            '''


            #optimal approach
        hashmap={}

        for words in strs:
            count=[0]*26

            for i in words:
                ind=ord(i)-ord('a')
                count[ind]+=1
                #[2,0,1,0....]:[aca,caa]
            key=tuple(count)
            if key not in hashmap:
                hashmap[key]=[]
            hashmap[key].append(words)
        return list(hashmap.values())




        