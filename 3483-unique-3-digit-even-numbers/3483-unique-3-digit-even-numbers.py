from collections import Counter

class Solution(object):
    def totalNumbers(self, digits):
        digit_counts = Counter(digits)
        valid_count = 0
        for num in range(100, 1000, 2):
            num_counts = Counter([int(d) for d in str(num)])
            if all(digit_counts[d] >= count for d, count in num_counts.items()):
                valid_count += 1
                
        return valid_count