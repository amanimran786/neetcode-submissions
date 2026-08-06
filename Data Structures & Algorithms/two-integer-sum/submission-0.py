class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """
        Optimal solution using hash map - O(n) time, O(n) space
        
        Approach:
        - For each number, calculate complement needed
        - Check if complement already seen
        - Store number for future lookups
        
        Args:
            nums: List of integers
            target: Target sum
            
        Returns:
            List of two indices where nums[i] + nums[j] == target
        """
        # Dictionary to store value -> index mapping
        seen = {}
        
        for i, num in enumerate(nums):
            # What number do we need to reach target?
            complement = target - num
            
            # Have we already seen this complement?
            if complement in seen:
                return [seen[complement], i]
            
            # Store current number for future reference
            seen[num] = i
        
        # Should not reach here per problem constraints
        return []