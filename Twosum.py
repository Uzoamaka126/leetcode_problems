'''
First Pass

Loop through list twice checking if the sum at each iteration is equal to the target

Time Complexity => O(n^2)
Space Complexity => O(1)
'''


def two_sum_1(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


'''
Second Pass

Using a dictionary as a hashtable, loop through the list. At each iteration, 
check if the complementary number is in the hashtable, if it's  not
store the current number as a key in the hashtable with the index as the value.
If it is return the value in the hashtable and the current index.


Time Complexity => O(n^2)
Space Complexity => O(1)
'''


def two_sum_2(nums, target):
    hash_table = {}
    for i, num in enumerate(nums):
        difference = target - num

        if difference in hash_table:
            return [hash_table[difference], i]
        hash_table[num] = i
    return []


two_sum_2([2, 3, 4, 4, 5, 6], 11)
