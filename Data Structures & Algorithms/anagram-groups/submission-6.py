class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)

        for s in strs:
            charmap = [ord('a') - ord('a')] * 26

            for c in s:
                charmap[ord(c) - ord('a')] += 1

            result[tuple(charmap)].append(s)

        return [x for x in result.values()]



