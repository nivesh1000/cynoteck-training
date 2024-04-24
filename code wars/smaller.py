def count_smaller_numbers(nums):
    def merge_sort(enum):
        half = len(enum) // 2
        if half:
            left, right = merge_sort(enum[:half]), merge_sort(enum[half:])
            for i in reversed(range(len(enum))):
                if not right or left and left[-1][1] > right[-1][1]:
                    smaller[left[-1][0]] += len(right)
                    enum[i] = left.pop()
                else:
                    enum[i] = right.pop()
        return enum

    smaller = [0] * len(nums)
    merge_sort(list(enumerate(nums)))
    return smaller

# Test the function
nums = [2, 3, 1]
result = count_smaller_numbers(nums)
print(result)