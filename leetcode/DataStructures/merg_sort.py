
def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divid: Find the midpount of the list and divide into sublists
    Conquer: Recursively sort the sublists created in previous step
    Combine: Merge the sorted sublists created in previous step


    Takes O(n log n)
    """

    if len(list) <= 1:  # Stopping Condition, if the list only has one object it has already been sorted
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left,right) 

def split(list):
    """
    Divid the unsorted list at midpoint into sublists
    Returns two sublists - left and right

    Takes overall O(log n)
    """

    mid = len(list) // 2  # // <-- floor division operator
    left = list[:mid] # start at : and stop add mid variable, python interprests : depending on positionstart/stop
    right = list[mid:]

    return left,right

def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list

    Runs in overall O(n) time
    """

    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]: 
            l.append(left[i])
            i  += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i += 1
    while j < len(right):
        l.append(right[j])
        j += 1
    
    return l

def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    
    return list[0] < list[1] and verify_sorted(list[1:])


alist = [54, 26, 97, 23, 15, 24, 56]

l = merge_sort(list=alist)
print(verify_sorted(alist))
print(verify_sorted(l))