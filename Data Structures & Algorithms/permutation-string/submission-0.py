class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        
        if n1 > n2:
            return False
        
        count1 = Counter(s1)
        window = Counter(s2[:n1])
        
        if window == count1:
            return True
        
        for i in range(n1, n2):
            # add new char
            window[s2[i]] += 1
            
            # remove old char
            left_char = s2[i - n1]
            window[left_char] -= 1
            
            if window[left_char] == 0:
                del window[left_char]
            
            if window == count1:
                return True
        
        return False