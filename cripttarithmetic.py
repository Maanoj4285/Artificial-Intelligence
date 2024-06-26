import itertools

def is_valid_solution(words, result, char_to_digit):
    # Replace characters with digits in words and result
    words_with_digits = [''.join(char_to_digit[char] for char in word) for word in words]
    result_with_digits = ''.join(char_to_digit[char] for char in result)

    # Convert to integers
    word_values = [int(word) for word in words_with_digits]
    result_value = int(result_with_digits)

    # Check if the sum of words equals the result
    if sum(word_values) == result_value:
        return True
    return False

def solve_cryptarithm(equation):
    # Split equation into parts
    left_side, right_side = equation.split('=')
    words = [word.strip() for word in left_side.split('+')]
    result = right_side.strip()

    # Extract unique characters
    unique_chars = set(''.join(words) + result)

    if len(unique_chars) > 10:
        raise ValueError("Too many unique characters, more than 10 digits needed")

    # Try all permutations of digits for the unique characters
    for perm in itertools.permutations('0123456789', len(unique_chars)):
        char_to_digit = dict(zip(unique_chars, perm))

        # Skip if any word or result starts with a zero
        if any(char_to_digit[word[0]] == '0' for word in words + [result]):
            continue

        # Check if this permutation is a valid solution
        if is_valid_solution(words, result, char_to_digit):
            print(f"Valid permutation found: {char_to_digit}")
            return char_to_digit

    return None

def main():
    equation = "SEND + MORE = MONEY"
    solution = solve_cryptarithm(equation)

    if solution:
        print(f"Solution for {equation}:")
        for char, digit in solution.items():
            print(f"{char} = {digit}")
    else:
        print(f"No solution found for {equation}")

if __name__ == "__main__":
    main()
