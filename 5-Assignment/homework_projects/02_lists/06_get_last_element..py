"""Fill out the function get_last_element(lst) which takes in a list lst as a parameter and prints the last element in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length"""




def get_last_element(lst):
    print(lst[-1])


user_input = input("Enter list of numbers separated by commas: ")
get_last_element(user_input)