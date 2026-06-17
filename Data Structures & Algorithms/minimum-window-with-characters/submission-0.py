class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        window = {}
        have, required = 0, len(need)
        left = 0
        best_start, best_len = 0, float('inf')

        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1

            # Check if this char's requirement is now satisfied
            if c in need and window[c] == need[c]:
                have += 1

            # Try to shrink the window while it's valid
            while have == required:
                # Update best result
                if (right - left + 1) < best_len:
                    best_len = right - left + 1
                    best_start = left

                # Shrink from left
                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    have -= 1
                left += 1

        return s[best_start : best_start + best_len] if best_len != float('inf') else ""