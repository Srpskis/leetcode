"""

Description:

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Category : easy

------------------------------------------------------------------------------------------------------------------------

Example:

Input: s = "()"
Output: true

Input: s = "()[]{}"
Output: true

Input: s = "(]"
Output: false

Input: s = "([)]"
Output: false

Input: s = "{[]}"
Output: true

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
------------------------------------------------------------------------------------------------------------------------
"""

def valid_parentheses(s):
    if len(s) % 2 == 1:
        return False

    dict = {")": "(", "}": "{", "]": "["}
    stack = []

    for each in s:
        if each in dict:
            if stack:
                element = stack.pop()
            else:
                element = "!"

            if dict[each] != element:
                return False
        else:
            stack.append(each)

    return not stack

