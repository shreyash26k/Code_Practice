class Solution(object):
    def minimumPushes(self, word):
        freq_dict = {}
        for letter in word:
            if letter in freq_dict:
                freq_dict[letter] = freq_dict[letter] + 1
            else:
                freq_dict[letter] = 1
        freq_list = list(freq_dict.values())
        freq_list.sort(reverse=True)
        total_pushes = 0
        for i in range(len(freq_list)):
            f = freq_list[i]
            pushes_per_letter = (i // 8) + 1
            total_pushes = total_pushes + (pushes_per_letter * f)

        return total_pushes