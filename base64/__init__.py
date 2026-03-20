import string

# Define red for error messages
red = "\033[91m"

# Lexicographical character set (base 64)
char = list(string.digits + string.ascii_uppercase + string.ascii_lowercase + "_-")


def con(num, base):
    if base < 37 or base > 64:
        print(f"{red}IntegerError: Base must be between 37 and 64 ({base} given).")
        return

    # Start converting the number to the specified base
    result = []

    # Handle the case for zero separately
    if num == 0:
        result.append(char[0])

    while num > 0:
        remainder = num % base
        result.append(char[remainder])
        num //= base

    # Since we've collected digits in reverse order, reverse the result
    result.reverse()

    # Join the list into a string and return
    print(''.join(result))

