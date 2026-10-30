
import math

print("================================")
print("Select the shape to calculate the area:")
print("================================")
print("1. Rectangle")
print("2. Square")
print("3. Triangle")
print("4. Circle")
print("5. parallelogram")
print("6. Trapezoid")
print("7. Oval")
print("8. Right Angle Triangle")
print("9. Rhombus")
print("0. Exit Program")

while True:
    choice = input("\nEnter your choice (0-9): ")

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

    elif choice == "5":
        base = float(input("Enter the base length: "))
        height = float(input("Enter the height: "))

        if base <= 0 or height <= 0:
            print("Please enter a number greater than 0")
            continue

        area = base * height
        print(f"Area of parallelogram = {area:.2f} square units")

    elif choice == "6":
        base1 = float(input("Enter the first base length: "))
        base2 = float(input("Enter the second base length: "))
        height = float(input("Enter the height: "))

        if base1 <= 0 or base2 <= 0 or height <= 0:
            print("Please enter a number greater than 0")
            continue

        area = 0.5 * (base1 + base2) * height
        print(f"Area of Trapezoid = {area:.2f} square units")

    elif choice == "7":
        major_axis = float(input("Enter the length of the major axis: "))
        minor_axis = float(input("Enter the length of the minor axis: "))

        if major_axis <= 0 or minor_axis <= 0:
            print("Please enter a number greater than 0")
            continue

        area = math.pi * major_axis * minor_axis
        print(f"Area of Oval = {area:.2f} square units")

    elif choice == "8":
        base = float(input("Enter the base length: "))
        height = float(input("Enter the height: "))

        if base <= 0 or height <= 0:
            print("Please enter a number greater than 0")
            continue

        area = 0.5 * base * height
        print(f"Area of Right Angle Triangle = {area:.2f} square units")

    elif choice == "9":
        diagonal1 = float(input("Enter the length of the first diagonal: "))
        diagonal2 = float(input("Enter the length of the second diagonal: "))

        if diagonal1 <= 0 or diagonal2 <= 0:
            print("Please enter a number greater than 0")
            continue

        area = 0.5 * diagonal1 * diagonal2
        print(f"Area of Rhombus = {area:.2f} square units")

    else:
        print("Invalid choice. Please select a valid option.")