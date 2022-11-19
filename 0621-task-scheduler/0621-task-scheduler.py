class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = collections.Counter(tasks)
        result = 0
        
        while True:
            sub_count = 0
            
            for task, _ in counts.most_common(n+1):
                sub_count += 1
                result += 1
                
                # reduce 1 from the counts of this iteration's task
                counts.subtract(task)
                # remove used up task
                counts += collections.Counter()
            
            if not counts:
                break
            
            result += n - sub_count + 1
        
        
        return result