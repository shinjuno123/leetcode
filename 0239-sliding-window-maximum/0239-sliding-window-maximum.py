class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res, deq = [], collections.deque()
        
        for i in range(len(nums)):
            # keep the size of window
            if deq and i - deq[0] == k:
                deq.popleft()
            
            # keep the index 0 of deq as a maximum value
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            
            # push index number to deq
            deq.append(i)
            
            # when the index is last of window, push max value to result
            if i + 1 >= k:
                res.append(nums[deq[0]])
        
        
        return res