"""
Given a list of n numbers, determine if it contains any duplicate numbers.
 Find the middle item in a singly linked list, or two middle items if it contains an even number of nodes.
 Find the longest substring of unique letters in a given string of n letters. 
Given a string of text and a number k, find the k words in the given text that appear most frequently. Return the words in a new array sorted in decreasing order.


Luke
Psuedocode:
Create an empty list
Loop through numbers and add to empty list
If number already in list remove it
Return new list containing dupes

"""

# {
# 	2: -1,
# 	3: -1,
# 	5: -1,
# }

nums = [1, 1, 2, 3, 4, 4, 5, 6, 6]


def dupes(ls):
    dupe = {}
    for i in ls:
        if dupe.get(ls[i], 0) == 0:
            dupe[ls[i]] = -1
        else:
            del dupe[ls[i]]
    return dupe.keys()


dupes(nums)
