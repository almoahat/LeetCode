class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        
        if len(word1) == len(word2):
            for a in range(0, len(word1)):
                res += word1[a] + word2[a]
                    
        elif len(word1) > len(word2):
            idx = 0
            for a in range(0, len(word2)):
                res += word1[a] + word2[a]
                idx = a
            idx+=1       
            res+= word1[idx:]
                
        else:
            idx = 0
            for a in range(0, len(word1)):
                res += word1[a] + word2[a]
                idx = a
            idx+=1   
            res+= word2[idx:]
        
        return res