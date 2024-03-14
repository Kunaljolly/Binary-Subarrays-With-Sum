class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        count = 0
        prefix_sum = {0: 1}
        current_sum = 0
        
        for num in nums:
            current_sum += num
            count += prefix_sum.get(current_sum - goal, 0)
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        
        return count
