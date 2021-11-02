#LEETCode:
#longest common Prefix: 
"""
Runtime: 32 ms, faster than 86.52% of Python3 online submissions for Longest Common Prefix.
Memory Usage: 14.5 MB, less than 25.07% of Python3 online submissions for Longest Common Prefix.
TODO: Think of optimization.. 
"""


#!/usr/bin/env python3

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return (strs[0])
        
        longest_str = []
        min_len = len(strs[0])
        if len(strs) > 1:
            for var in strs[1:]:
                if len(var) < min_len:
                    min_len = len(var)
        for i in range(min_len):
            for j in strs:
                longest_str.append(j[i])
        ini  = 0
        final_str = []
        for _ in range(len(longest_str)):
            zz = (longest_str[ini:len(strs)+ini])
            ini += len(strs)
            if len(set(zz)) == 1:
                final_str.append((zz[0]))
            else:
                return("".join(final_str))
                

        return("".join(final_str))
                
