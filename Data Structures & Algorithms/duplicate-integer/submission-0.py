class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        result = []
        for num in nums:
            if num in seen:
                return True
            if not num in seen:
                seen.add(num)
                result.append(num)
        return False