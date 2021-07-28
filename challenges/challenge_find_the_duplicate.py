def QuickSort(entry_list):
    if len(entry_list) == 0:
        return entry_list
    pivot = entry_list[0]
    front = QuickSort(
        [smaller for smaller in entry_list[1:] if smaller <= pivot])
    behind = QuickSort([larger for larger in entry_list[1:] if larger > pivot])
    return front + [pivot] + behind


"""
https://www.delftstack.com/pt/howto/
python/python-find-duplicates-in-list/
"""


def find_duplicate(nums):
    if len(nums) <= 1 or isinstance(nums, str):
        return False
    result = QuickSort(nums)
    repeated = list(
        set([num for num in result if result.count(num) > 1 and num > 0]))

    if len(repeated) != 1:
        return False
    return repeated[0]
