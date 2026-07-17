class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        tracker_s = {}
        tracker_t = {}

        for char in s:
            if char in tracker_s:
                tracker_s[char] += 1
            else:
                tracker_s[char] = 1
        for char in t:
            if char in tracker_t:
                tracker_t[char] += 1
            else:
                tracker_t[char] = 1
            
        return tracker_s == tracker_t