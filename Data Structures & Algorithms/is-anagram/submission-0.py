class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## Need something that reads each character
        ## And if each character has the same then returns true once loop finishes

        ## If they aren't the same length they can't be anagrams
        if len(s) != len(t):
            return False

        ## Create 2 empty dictionaries
        tracker_s = {}
        tracker_t = {}

        for char in s:
            tracker_s[char] = tracker_s.get(char, 0) + 1
        for char in t:
            tracker_t[char] = tracker_t.get(char, 0) + 1               

        return tracker_s == tracker_t

        