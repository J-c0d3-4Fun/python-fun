def binary_search(list,target):
    """
    
    """
    first = 0 
    last = len(list) - 1 # tkaes the number of elements in the list, the list starts at 0.
    
    while first <= last:
        midpoint = (first + last)//2 # Floor division operator that rounds to the nearest whole number

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in list")

numbers = [1,2,3,4,5,6,8,8,9,10] # <-- has to be sorted if unsorted the implemnetation may return None even if the value is there

result = binary_search(numbers, 12)
verify(result)


result = binary_search(numbers, 6)
verify(result)