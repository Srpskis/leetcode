"""

Title: Isomorphic strings

Description: Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"

Output: true

Explanation:

The strings s and t can be made identical by:

Mapping 'e' to 'a'.
Mapping 'g' to 'd'.
Example 2:

Input: s = "f11", t = "b23"

Output: false

Explanation:

The strings s and t can not be made identical as '1' needs to be mapped to both '2' and '3'.

Example 3:

Input: s = "paper", t = "title"

Output: true

 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

Thougth process:

Looks like we can iterate over the letters of the first word and map it in the dictionary with the
same index of the second word, if not mapped already.

1. Initialize the dictionary to store mapping
2. Iterate over first word
    3. If character in word exists as a key in dictionary
        4. and the value is not the same as character under index in second word
            5. return false
    5. otherwise add it to dictionary
6. return true

"""

def isomorphic_strings1(word1, word2):
    word1_to_word2 = {}
    word2_to_word1 = {}
    for char1, char2 in zip(word1, word2):
        if word1_to_word2.get(char1, char2) != char2 or word2_to_word1.get(char2, char1) != char1:
            return False
        word1_to_word2[char1] = char2
        word2_to_word1[char2] = char1
    return True

def isomorphic_strings2(s, t):
    mapping = {}
    used = set()
    for c1, c2 in zip(s, t):
        if c1 in mapping:
            if mapping[c1] != c2:
                return False
        elif c2 in used:
            return False
        else:
            mapping[c1] = c2
            used.add(c2)
    return True

    
print(isomorphic_strings1("egg", "add"))
print(isomorphic_strings1("f11", "b23"))
print(isomorphic_strings1("paper", "title"))
print(isomorphic_strings1("badc", "baba"))
