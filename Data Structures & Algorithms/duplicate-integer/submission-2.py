class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()        ## Create empty set for duplicates
        for num in nums:
            if num in seen:
                return True
            if not num in seen:
                seen.add(num)
        return False
