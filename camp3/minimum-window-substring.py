class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ht = Counter(t)
        window = Counter()
        bl, br = 0, float("inf")
        left = 0

        for right in range(len(s)):
            window[s[right]] += 1

            while window & ht == ht:
                window[s[left]] -= 1

                if window[s[left]] == 0:
                    del window[s[left]]

                if right - left < br - bl:
                    bl, br = left, right

                left += 1

        return s[bl:br+1] if br != float("inf") else ""
