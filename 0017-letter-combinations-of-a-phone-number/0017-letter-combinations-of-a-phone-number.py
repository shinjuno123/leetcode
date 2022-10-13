class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        table = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }
        if len(digits) == 0:
            return
        
        res = []
        
        def dfs(combin, k, index):
            if k == 0:
                res.append(combin)
                return
            
            for c in table[digits[index]]:
                dfs(combin + c, k - 1, index + 1)
        
        
        dfs("",len(digits),0)
        
        return res