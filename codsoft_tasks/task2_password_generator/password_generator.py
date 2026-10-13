"""Task 2: Password Generator (CODSOFT Python Internship)."""

import secrets
import string

MIN_LENGTH = 4
MAX_LENGTH = 128


def ask_length() -> int:
    while True:
        try:
            length = int(input(f"Password length ({MIN_LENGTH}-{MAX_LENGTH}): "))
            if MIN_LENGTH <= length <= MAX_LENGTH:
                return length
            print(f"  Please enter a value between {MIN_LENGTH} and {MAX_LENGTH}.")
        except ValueError:
            print("  Please enter a whole number.")


def ask_yes_no(question: str, default: bool = True) -> bool:
    hint = "Y/n" if default else "y/N"
    answer = input(f"{question} [{hint}]: ").strip().lower()
    return default if not answer else answer.startswith("y")


def generate_password(length: int, use_upper=True, use_digits=True, use_symbols=True) -> str:
    """Generate a random password containing at least one char from each chosen set."""
    pools = [string.ascii_lowercase]
    if use_upper:
        pools.append(string.ascii_uppercase)
    if use_digits:
        pools.append(string.digits)
    if use_symbols:
        pools.append("!@#$%^&*()-_=+[]{};:,.<>?")

    # Guarantee one character from every selected pool
    chars = [secrets.choice(pool) for pool in pools]
    all_chars = "".join(pools)
    chars += [secrets.choice(all_chars) for _ in range(length - len(chars))]

    # Shuffle securely so the guaranteed characters aren't always first
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)


def strength(password: str) -> str:
    kinds = sum([
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(not c.isalnum() for c in password),
    ])
    score = kinds + (len(password) >= 12) + (len(password) >= 16)
    return "Weak" if score <= 2 else "Medium" if score <= 4 else "Strong"


def main() -> None:
    print("=== Password Generator ===")
    while True:
        length = ask_length()
        upper = ask_yes_no("Include uppercase letters?")
        digits = ask_yes_no("Include digits?")
        symbols = ask_yes_no("Include symbols?")

        password = generate_password(length, upper, digits, symbols)
        print(f"\nGenerated password: {password}")
        print(f"Strength: {strength(password)}")

        if not ask_yes_no("\nGenerate another?", default=False):
            print("Goodbye!")
            break
        print()


if __name__ == "__main__":
    main()
