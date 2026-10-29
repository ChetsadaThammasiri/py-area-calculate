
import math

print("================================")
print("Select the shape to calculate the area:")
print("================================")
print("1. Rectangle")
print("2. Square")
print("3. Triangle")
print("4. Circle")
print("0. Exit Program")

while True:
    choice = input("\nEnter your choice (0-4): ")

    if choice == "0":
        print("Thank you for using the program, Goodbye!")
        break

    elif choice == "1":
        width = float(input("Enter the width: "))
        length = float(input("Enter the length: "))

        if width <= 0 or length <= 0:
            print("Please enter a number greater than 0")
            continue

        area = width * length
        print(f"Area of Rectangle = {area:.2f} square units")

    elif choice == "2":
        side = float(input("Enter the side length: "))

        if side <= 0:
            print("Please enter a number greater than 0")
            continue

        area = side ** 2
        print(f"Area of Square = {area:.2f} square units")

    elif choice == "3":
        base = float(input("Enter the base length : "))
        height = float(input("Enter the height: "))

        if base <= 0 or height <= 0:
            print("Please enter a number greater than 0")
            continue

        area = 0.5 * base * height
        print(f"Area of Triangle = {area:.2f} square units")

    elif choice == "4":
        radius = float(input("Enter the radius of the circle: "))

        if radius <= 0:
            print("Please enter a number greater than 0")
            continue

        area = math.pi * radius ** 2
        print(f"Area of Circle = {area:.2f} square units")

    else:
        print("Invalid choice. Please select a valid option.")