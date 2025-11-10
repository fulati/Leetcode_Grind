class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        best_l, best_r = 0, 0  # inclusive bounds

        for i in range(n):
            # odd-length center at i
            l, r = i, i
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l > best_r - best_l:
                    best_l, best_r = l, r
                l -= 1
                r += 1

            # even-length center between i and i+1
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l > best_r - best_l:
                    best_l, best_r = l, r
                l -= 1
                r += 1

        return s[best_l:best_r + 1]
