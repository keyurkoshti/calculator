def add(numbers):
    return sum(numbers)

def sub(numbers):
    result = numbers[0]
    for num in numbers[1:]:
        result -= num
    return result

def mul(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

def div(numbers):
    result = numbers[0]
    try:
        for num in numbers[1:]:
            result /= num
    except ZeroDivisionError:
        return "Error! Division by zero."
    return result

while True:
    print("\n--- Menu ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    
    choice = int(input("Enter your choice: "))
    
    if choice == 5:
        print("Exiting the program. Goodbye!")
        break
    
    numbers = list(map(float, input("Enter numbers separated by spaces: ").split()))
    
    if len(numbers) < 2:
        print("Please enter at least two numbers.")
        continue

    if choice == 1:
        print("Result:", add(numbers))
    elif choice == 2:
        print("Result:", sub(numbers))
    elif choice == 3:
        print("Result:", mul(numbers))
    elif choice == 4:
        print("Result:", div(numbers))
    else:
        print("Invalid choice! Please select a valid option.")
