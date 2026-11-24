"""

Title: Fun With Anagrams

Description: You are given an array of strings. Two strings are considered anagrams if they contain exactly the same characters, just in different order: "aaagmnrs" is an anagram of "anagrams".
Your task is to process the array by removing any string that is an anagram of a string that appears earlier in the array. After removal, return the remaining strings in sorted order.

Example: text = ["code", "doce", "ecod", "framer", "frame"]; 
Processing: 
    "code" and "doce" are anagrams -> keep "code" and remove "doce". Result = ["code"]
    "code" and "ecod" are anagrams -> keep "code" and remove "ecod". Result = ["code"]
    "code" and "framer" are not anagrams -> keep both. Result = ["code", "framer"]
    "framer" and "frame" are not anagrams -> keep both. Result = ["code", "framer", "frame"]

    Return ["code", "frame", "framer"].

Pseudocode:

1. Construct empty `result` array
2. Construct empty `seen` set to store seen words when iterating over input array
2. Iterate over words in input array
    3. If sorted word does not exist in `seen` set
        4. Add the sorted word to `seen` set
        5. Appen the word to the result array
7. Return sorted result array

"""

from modulefinder import test


def fun_with_anagrams(words):
    seen = set()
    result = []

    for word in words:
        sorted_word = "".join(sorted(word))
        if sorted_word not in seen:
            seen.add(sorted_word)
            result.append(word)
    
    return sorted(result)

test1 = ["code", "doce", "ecod", "framer", "frame"]
test2 = []
test3 = ["code"]
test4 = ["code", "code"]
print(fun_with_anagrams(test1))
print(fun_with_anagrams(test2))
print(fun_with_anagrams(test3))
print(fun_with_anagrams(test4))

"""
Time complexity analysis: O(n * log(n))

Pattern: hash map keyed by a derived value.

"""