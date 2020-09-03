
"""

Description:

Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Category : easy

------------------------------------------------------------------------------------------------------------------------

Example:

Input: ["flower","flow","flight"]
Output: "fl"

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

------------------------------------------------------------------------------------------------------------------------
"""


def longest_common_prefix(strs):
    if len(strs) == 0:
        return ""

    min_string = min(strs)
    for i in range(0, len(min_string)):
        index_stop = i
        for each in strs:
            if each[i] == min_string[i]:
                continue
            else:
                if index_stop > 0:
                    result = ""
                    for j in range(0, index_stop):
                        result += min_string[j]
                    return result
                else:
                    return ""
    return min_string

