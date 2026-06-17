class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for s in strs:
            key = tuple(sorted(s))   # "pots" → ('o','p','s','t')
            groups[key].append(s)
        return list(groups.values())