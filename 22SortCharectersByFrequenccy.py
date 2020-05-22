from collections import Counter 

class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        mostCommon = count.most_common()
        output = ""
        for item in mostCommon:
            for j in range(0, item[1]):
                output += item[0]
        return output
