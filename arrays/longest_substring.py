#Given a string s, find the length of the longest substring without duplicate characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        start = 0
        max_length = 0
        for end in range(len(s)):
            current_char = s[end]
            if current_char in char_map and char_map[current_char] >= start:
                start = char_map[current_char] + 1
            char_map[current_char] = end
            current_length = end - start + 1
            max_length = max(max_length, current_length)
        return max_length
