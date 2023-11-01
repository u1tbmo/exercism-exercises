def rebase(input_base: int, digits: list, output_base: int) -> list:
    # Check for invalid input_base
    if input_base < 2:
        raise ValueError("input base must be >= 2")
    
    # Check for invalid output_base
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    
    # Check for invalid digits
    for digit in digits:
        if digit < 0 or digit >= input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")

    # Check if input_base is not 10 and convert to decimal
    number: int = 0
    if input_base != 10:
        number = convert_to_decimal(input_base, digits)
    else:
        number = int("".join([str(digit) for digit in digits]))

    # Convert to output_base
    result = []
    while number > 0:
        result.append(number % output_base)
        number //= output_base

    return result[::-1] if result else [0]

def convert_to_decimal(input_base: int, digits: list) -> int:
    decimal = 0
    for i, digit in enumerate(digits[::-1]):
        decimal += int(digit) * input_base ** i
    return decimal
