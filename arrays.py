def min_max(nums):
    if nums == []:
        return "ValueError"
    else:
        return min(nums), max(nums)


print(min_max([3, -1, 5, 5, 0]))


def unique_sorted(nums1):
    if len(nums1) > 0:
        return sorted(set(nums1))


print(unique_sorted([-1, -1, 0, 2, 2]))


def flatten(nums2):
    ans = []
    for i in nums2:
        if isinstance(i, list) or isinstance(i, tuple):
            for j in i:
                ans.append(j)
        else:
            ans = "TypeError"
    return ans


print(flatten([(1, 2), [3, 4, 5]]))
