class SelectionSort:
    def sort(self, nums: list) -> list:
        for i in range(len(nums)):
            min_idx = i
            for j in range(i + 1, len(nums)):
                if nums[min_idx] > nums[j]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
        return nums

nums = [99, 88, 77, 66, 55, 44, 33, 22, 11]
print("array to sort:", nums)

selection = SelectionSort()
print(selection.sort(nums))

