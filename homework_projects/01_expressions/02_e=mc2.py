"""Write a program that continually reads in mass from the user and then outputs the equivalent energy using Einstein's mass-energy equivalence formula (E stands for energy, m stands for mass, and C is the speed of light:

E = m * c**2

Almost 100 years ago, Albert Einstein famously discovered that mass and energy are interchangeable and are related by the above equation. You should ask the user for mass (m) in kilograms and use a constant value for the speed of light -- C = 299792458 m/s.

Here's a sample run of the program (user input is in bold italics):

Enter kilos of mass: 100

e = m * C^2...

m = 100.0 kg

C = 299792458 m/s

8.987551787368176e+18 joules of energy!"""


light_speed = 299792458 


def mass_to_energy():
    try:
      mass = float(input("Enter the mass :"))
      energy = mass * light_speed ** 2
      print("\ne = m * C^2...\n")
      print(f"m = {mass} kg")
      print(f"C = {light_speed} m/s")
      print(f"e = {energy} J")
    except ValueError:
       print("Please enter a valid number")
    except KeyboardInterrupt:
         print("\n\nYou have exited the program\n\n")
mass_to_energy()