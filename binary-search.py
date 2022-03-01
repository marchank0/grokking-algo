def bsearch(objects: list, target: int) -> int:
    low = 0
    high = len(objects) - 1

    while (low <= high):
        mid = int((low + high) / 2)
        guess = objects[mid]
        if (guess == target):
            return mid
        if (guess > target):
            high = mid
        else:
            low = mid + 1 
    return None

objects = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 8
print("binary search input:", objects, target, "answer: 7")
print(bsearch(objects, target))

