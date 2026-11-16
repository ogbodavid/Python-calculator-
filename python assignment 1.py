#calculator

while True:
    print("\n===== MATHEMATICS CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")



    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    addition = a + b

    subtraction = a - b

    multiplication = a * b

    division = a / b

    choice = input("Choose an operation: ")
    if choice == "1":
        print(addition)
    elif choice == "2":
        print(subtraction)
    elif choice == "3":
        print(multiplication)
    elif choice == "4":
        print(division)
    else:
        print("Invalid choice!")

    repeat = input("Do you want to continue? (y / n): ")
    if repeat.lower() == "n":
     print("Calculator closed!")
     break
    elif repeat.lower() == "y":
        continue

