"""

Title: Valid Anagram

Description: Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Pseudocode:

1. Sort both string
2. Compare
3. Retrun result

"""

def valid_anagram(string1, string2):
    return "".join(sorted(string1)) == "".join(sorted(string2))

print(valid_anagram("anagram", "nagaram"))
print(valid_anagram("rat", "car"))




"""
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

Example: 

s = "U+00FC"
t = "U+F0F0C"


"""

print(valid_anagram("U+00FC", "U+F0F0C"))