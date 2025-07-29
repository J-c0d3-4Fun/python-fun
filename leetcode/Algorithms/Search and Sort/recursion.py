def sum(numbers):
    if not numbers:
        return 0
    remaining_sum = sum(numbers[1:]) # slice notation to grab all numbers except the first "0"
    return numbers[0] + remaining_sum



print(sum([1,2,7,9]))