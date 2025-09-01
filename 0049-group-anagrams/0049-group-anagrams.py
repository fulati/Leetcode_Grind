class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = defaultdict(list)

        for i in range(len(strs)):

            output[''.join(sorted(strs[i]))].append(strs[i])

        return list(output.values())