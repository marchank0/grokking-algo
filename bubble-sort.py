class BubbleSort:
    def sort(self, nums: list) -> list:
        for i in range(len(nums) - 1):
            for j in range(0, len(nums) - i - 1):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

nums = [99, 88, 77, 66, 55, 44, 33, 22, 11]
print("array to sort:", nums)
bubble = BubbleSort()
print(bubble.sort(nums))

