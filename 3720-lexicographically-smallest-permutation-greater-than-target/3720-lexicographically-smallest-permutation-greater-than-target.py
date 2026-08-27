from collections import Counter

class Solution(object):
    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        counts = Counter(s)
        prefix = []

        def solve(idx):
            if idx == n:
                return False  # Equal to target, not strictly greater

            char = target[idx]

            # Try exact match first
            if counts[char] > 0:
                counts[char] -= 1
                prefix.append(char)
                if solve(idx + 1):
                    return True
                prefix.pop()
                counts[char] += 1

            # Try smallest character strictly greater than target[idx]
            for c in sorted(counts.keys()):
                if c > char and counts[c] > 0:
                    prefix.append(c)
                    counts[c] -= 1

                    # Fill remainder with smallest available characters
                    for rem_char in sorted(counts.keys()):
                        prefix.extend([rem_char] * counts[rem_char])
                    return True

            return False

        if solve(0):
            return "".join(prefix)
        return ""
        