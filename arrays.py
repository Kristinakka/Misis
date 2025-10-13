def min_max(nums):
    if len(nums) == 0:
        return ValueError
    else:
        return min(nums) and max(nums)


def unique_sorted(nums1):
    if len(nums1) > 0:
        return set(len(nums1))


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
