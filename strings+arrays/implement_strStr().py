"""

Description:

Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Constraints:

haystack and needle consist only of lowercase English characters.

Category : easy

------------------------------------------------------------------------------------------------------------------------

Example:

Input: haystack = "hello", needle = "ll"
Output: 2

Input: haystack = "aaaaa", needle = "bba"
Output: -1

What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr()
and Java's indexOf().

------------------------------------------------------------------------------------------------------------------------
"""


def str_str(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle == "":
        return 0
    if len(needle) > len(haystack):
        return -1

    if needle in haystack:
        for i in range(0, len(haystack)):
            if haystack[i: len(needle) + i] == needle:
                return i

    else:
        return -1

