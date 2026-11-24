"""

Title: Group Anagrams

Description: Given an array of strings strs, group the anagrams together. You can return the answer in any order.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]

 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.

Pseudocode:

1. Initiate empty disctionary to store sorted word to array of anagrams for that word
2. Initiate empty result array to store groups of words that are anagrams
3. Iterate over words in input array
    4. Sort word
    5. Check if dictionary has a sorted word
        6. If no, add the sorted word to dictionary as sorted_word:  [word]
        7. If yes, add a word to sorted dictionary value array under word key
8. Iterate over dictionary values and store them in the result array
9. Retunr result array


"""

from tokenize import String


def group_anagrams(words):
    seen = {}

    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word not in seen:
            seen[sorted_word] = [word]
        else:
            seen[sorted_word].append(word)
    
    return list[String](seen.values())

words = ["eat","tea","tan","ate","nat","bat"]
print(group_anagrams(words))

"""
Time complexity: O(n)
Pattern: hash map keyed by a derived value.

"""