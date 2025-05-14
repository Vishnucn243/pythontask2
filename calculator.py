def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "zero division error"

def calculator():
    while True:
        print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
        choice = input("Enter choice  ")
        if choice == '5':
            print("Exiting")
            break
        if choice not in ['1', '2', '3', '4']:
            print("Invalid ")
            continue
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        if choice == '1':
            print(f"Result: {add(a, b)}")
        elif choice == '2':
            print(f"Result: {subtract(a, b)}")
        elif choice == '3':
            print(f"Result: {multiply(a, b)}")
        elif choice == '4':
            print(f"Result: {divide(a, b)}")

if __name__ == "__main__":
    calculator()