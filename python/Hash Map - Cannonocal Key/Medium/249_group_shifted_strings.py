"""
Problem Description:

You are given an array of strings and need to group strings that belong to the same "shifting sequence".

A shifting sequence is formed by repeatedly shifting letters in a string:

Right shift: Replace each letter with the next letter in the alphabet (a→b, b→c, ..., z→a)
Left shift: Replace each letter with the previous letter in the alphabet (b→a, c→b, ..., a→z)
For example, the strings "abc", "bcd", "xyz", "yza", and "zab" all belong to the same shifting sequence because:

"abc" can be right-shifted to "bcd"
"bcd" can be right-shifted multiple times to eventually get "xyz"
"xyz" can be right-shifted to "yza"
"yza" can be right-shifted to "zab"
"zab" can be right-shifted to "abc" (completing the cycle)

Example:

Input: ["abc","bcd","acef","xyz","az","ba","a","z"]
Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]

"""

from collections import defaultdict


def groupStrings(words):
    groups = defaultdict(list)
    for word in words:
        distances = []
        for i in range(0, len(word)-1):
            distance = ord(word[i+1]) - ord(word[i])
            if distance < 0:
                distances.append(distance + 26)
            else:
                distances.append(distance)
        distances_tuple = tuple(distances)
        groups[distances_tuple].append(word)
    return list(groups.values())


words = ["abc","bcd","acef","xyz","az","ba","a","z"]
print(groupStrings(words))