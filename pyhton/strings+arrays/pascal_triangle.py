
"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

"""


def generate(numRows):
    """
    :type numRows: int
    :rtype: List[List[int]]
    """

    if numRows == 0:
        return []
    if numRows == 1:
        return [[1]]
    if numRows == 2:
        return [[1], [1, 1]]

    base = [[1], [1, 1]]
    for i in range(0, numRows - 2):
        index = len(base) - 1
        i = 0
        new_addition = [1]
        while i < len(base[index]) - 1:
            new_addition.append(base[index][i] + base[index][i + 1])
            i += 1
        new_addition.append(1)
        base.append(new_addition)
    return base


num = 6
matrix = generate(num)
print(matrix)
