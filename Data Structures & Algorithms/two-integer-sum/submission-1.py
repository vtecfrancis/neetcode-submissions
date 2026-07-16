class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}       # Dictionary to store {number: index}

        for i in range(len(nums)):
            current_num = nums[i]
            # Calculate the complement (what we need to reach the target)
            complement = target - current_num

            # Check if we seen complement before
            if complement in seen:
                # Hint: How do you look up the complement's index in the seen dictionary?
                # Return the index of the complement and current index i
                return [seen[complement], i]
            
            # If not, save current number and its index for the future
            seen[current_num] = i