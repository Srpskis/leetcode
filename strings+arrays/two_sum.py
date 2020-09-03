"""

Description:    Given an array of integers nums and and integer target, return the indices of the two numbers such that
                they add up to target.
                You may assume that each input would have exactly one solution, and you may not use the same element twice.
                You can return the answer in any order.
                Category : easy

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

------------------------------------------------------------------------------------------------------------------------
Input: - array of integers
       - integer (target)

Output: indices of two numbers such that they add up to target

------------------------------------------------------------------------------------------------------------------------

Example:

    Input: nums = [2,7,11,15], target = 9
    Output: [0,1]
    Output: Because nums[0] + nums[1] == 9, we return [0, 1]

    Input: nums = [3,2,4], target = 6
    Output: [1,2]

    Input: nums = [3,3], target = 6
    Output: [0,1]

------------------------------------------------------------------------------------------------------------------------
"""

#

def two_sum(nums, target):
    target_dict = {}
    result = []

    for i in range(0, len(nums)):
        num = target - nums[i]
        if num not in target_dict:
            target_dict[nums[i]] = i
        else:
            result.append(target_dict[num])
            result.append(i)
            return result
    return result

