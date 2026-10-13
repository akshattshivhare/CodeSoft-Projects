"""Task 1: Simple Command-Line Calculator (CODSOFT Python Internship)."""

OPERATIONS = {
    "+": ("Addition", lambda a, b: a + b),
    "-": ("Subtraction", lambda a, b: a - b),
    "*": ("Multiplication", lambda a, b: a * b),
    "/": ("Division", lambda a, b: a / b),
    "%": ("Modulus", lambda a, b: a % b),
    "**": ("Power", lambda a, b: a ** b),
}


def read_number(prompt: str) -> float:
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  Invalid number, please try again.")


def show_menu() -> None:
    print("\nAvailable operations:")
    for symbol, (name, _) in OPERATIONS.items():
        print(f"  {symbol:<3} {name}")


def format_result(value: float):
    return int(value) if float(value).is_integer() else round(value, 6)


def main() -> None:
    print("=== Simple Calculator ===")
    while True:
        a = read_number("\nEnter first number: ")
        b = read_number("Enter second number: ")
        show_menu()
        op = input("Choose an operation: ").strip()

        if op not in OPERATIONS:
            print("  Invalid operation. Try again.")
            continue

        name, func = OPERATIONS[op]
        try:
            result = func(a, b)
            print(f"\n{name}: {format_result(a)} {op} {format_result(b)} = {format_result(result)}")
        except ZeroDivisionError:
            print("\n  Error: cannot divide by zero.")
        except OverflowError:
            print("\n  Error: result is too large.")

        again = input("\nDo another calculation? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
