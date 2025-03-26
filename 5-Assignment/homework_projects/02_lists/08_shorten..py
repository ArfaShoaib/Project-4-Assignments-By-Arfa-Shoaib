"""Fill out the function shorten(lst) which removes elements from the end of lst, which is a list, and prints each item it removes until lst is MAX_LENGTH items long. If lst is already shorter than MAX_LENGTH you should leave it unchanged. We've written a main() function for you which gets a list and passes it into your function once you run the program. For the autograder to pass you will need MAX_LENGTH to be 3, but feel free to change it around to test your program."""


def shorten(lst):
    max_length = 3
    while len(lst) > max_length:
        removed = lst.pop()
        print(f"Removing {removed} from the list.")

    print(f"Here is the shortened list: {lst}")

def main():
    user_input = input("Enter a list of numbers separated by spaces: ")
    user_input = user_input.replace(",", " ").split()  # Fix input handling
    shorten(user_input)

main()
