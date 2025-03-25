"""Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural."""





inches_in_foot : int = 12

def feet_to_inches():
    feet = float(input("Enter the feet :"))
    inches = feet * inches_in_foot
    print(f"inches : {inches}")

feet_to_inches()