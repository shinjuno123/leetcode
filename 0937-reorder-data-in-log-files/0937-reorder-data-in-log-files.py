class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        # distinguish digit logs and letter logs
        digit_logs = []
        letter_logs = []
        
        for log in logs: # O(n)
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        
        
        # sort letter logs in lexical order. If contents are the same, sort them by identifiers.
        letter_logs.sort(key=lambda x:(x.split()[1:],x.split()[0])) # O(n log n)
        
        
        # merge letter_logs with digit_logs.(letter_logs first)
        return letter_logs + digit_logs
        
        
        