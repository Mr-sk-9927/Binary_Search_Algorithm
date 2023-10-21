def binary_search(array, target):
    left, right = 0, len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == target:
            return mid             # Target found, return its index.
        elif array[mid] < target:
            left = mid + 1         # Adjust the left bound.
        else:
            right = mid - 1        # Adjust the right bound.

    return -1                      # Target not found in the list.

#  Take Input list from the user
input_list = input("Enter a Sorted List : ")
array = [int(x) for x in input_list.split(",")]

# Input target value from the user
target = int(input("Enter the Target : "))

result = binary_search(array, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the list.")
