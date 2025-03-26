"""Write a program that doubles each element in a list of numbers. For example, if you start with this list:

numbers = [1, 2, 3, 4]

You should end with this list:

numbers = [2, 4, 6, 8]"""




def double_numbers(num):
    double_list = []
    for numbers in num:
        double_list.append(numbers * 2)
    return double_list


calculate = double_numbers([1, 2, 3, 4])
print(calculate)  