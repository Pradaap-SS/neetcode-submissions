class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded = ""
        for s in strs:
            encoded += f"{len(s)}#{s}"
        return encoded

    def decode(self, s: str) -> list[str]:
        result = []
        i = 0  # current position in the encoded string

        while i < len(s):
            # --- FIND THE LENGTH PREFIX ---
            # Scan forward from 'i' to find the '#' delimiter.
            # 'j' will land on the position of '#'.
            j = i
            while s[j] != '#':
                j += 1

            # Parse the integer length from the substring s[i:j].
            # e.g., if s[i:j] = "11", the next string has 11 characters.
            length = int(s[i:j])
            word = s[j + 1 : j + 1 + length]
            result.append(word)

            # --- ADVANCE THE POINTER ---
            # Move 'i' past: the length digits (j - i chars) + the '#' (1 char) + the content (length chars).
            # Equivalently: i = j + 1 + length
            i = j + 1 + length

        return result
