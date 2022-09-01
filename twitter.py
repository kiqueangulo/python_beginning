from functools import reduce

def sum_squares(numbers):
    return reduce(lambda prev, curr: prev + curr **  2 , numbers, 0)


def vanilla_sum_squares(numbers):
    result = 0

    for number in numbers:
        result += number ** 2
    
    return result

list_example = [1, 2, 2]

print(sum_squares(list_example))

print(vanilla_sum_squares(list_example))