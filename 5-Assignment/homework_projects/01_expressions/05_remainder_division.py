"""Ask the user for two numbers, one at a time, and then print the result of dividing the first number by the second and also the remainder of the division.

Here's a sample run of the program (user input is in bold italics):

Please enter an integer to be divided: 5

Please enter an integer to divide by: 3

The result of this division is 1 with a remainder of 2"""







def divider():
    while True:
        try:
            dividend = int(input("Enter a dividend: "))
            divider = int(input("Enter a divider: "))
            quotient = dividend // divider
            remainder = dividend % divider
            print(f"The result of {dividend} divided by {divider} is {quotient} with a remainder of {remainder}")
            break
        except ValueError:
            print("Please enter a valid number")
            continue
        except ZeroDivisionError:
            print("You cannot divide by zero")
            continue
        except KeyboardInterrupt:
            print("Goodbye")
            break

divider()