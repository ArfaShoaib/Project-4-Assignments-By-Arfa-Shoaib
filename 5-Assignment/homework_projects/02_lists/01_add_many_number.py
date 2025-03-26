"""Write a function that takes a list of numbers and returns the sum of those numbers."""




def add_numbers(numbers) -> int:
    total = 0
    for number in numbers:
        total += number
    return total


calculate = add_numbers([10 ,10,20])
print(calculate)  