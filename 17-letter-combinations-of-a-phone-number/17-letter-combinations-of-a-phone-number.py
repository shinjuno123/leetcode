class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = {
            "2" : 'abc',
            "3" : 'def',
            "4" : 'ghi',
            "5" : 'jkl',
            "6" : 'mno',
            "7" : 'pqrs',
            "8" : 'tuv',
            "9" : 'wxyz'
        }
        
        
        if not len(digits):
            return []
        
        res = []
        digits_cnt = len(digits)
        
        def dfs(idx, combination):
            
            if len(combination) == digits_cnt:
                res.append(combination)
                return
            
            for i in range(idx, digits_cnt):
                for alpha in table[digits[i]]:
                    dfs(i+1,combination + alpha)
                
        
        
        dfs(0,"")
            
        return res
        
     