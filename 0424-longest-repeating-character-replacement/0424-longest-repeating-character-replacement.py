class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        max_freq = 0
        ch = defaultdict(int)

        for r in range(len(s)):
            ch[s[r]] += 1

            max_freq = max(max_freq, ch[s[r]])

            if (r - l + 1) - max_freq > k:
                ch[s[l]] -= 1
                l += 1
            
            longest = max(longest, r - l + 1)
            
        return longest
