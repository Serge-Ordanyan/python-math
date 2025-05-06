import math

def large_factorial(n):
    """
    Calculates the factorial of a non-negative integer n.
    Handles potentially large results.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def large_power(base, exponent):
    """
    Calculates base raised to the power of exponent.
    Handles potentially large results.
    """
    if not isinstance(exponent, int):
        raise TypeError("Exponent must be an integer")
    return base ** exponent

def is_prime_large(n):
    """
    Checks if a positive integer n is a prime number.
    This version is suitable for moderately large numbers.
    """
    if not isinstance(n, int) or n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def fibonacci_large(n):
    """
    Generates the nth Fibonacci number using an iterative approach.
    Handles potentially large results.
    """
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

def combinations_large(n, k):
    """
    Calculates the number of combinations of choosing k items from a set of n items (nCk).
    Handles potentially large intermediate results.
    """
    if not isinstance(n, int) or not isinstance(k, int) or n < 0 or k < 0 or k > n:
        raise ValueError("Invalid input values")
    if k == 0 or k == n:
        return 1
    if k > n // 2:
        k = n - k

    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result

if __name__ == "__main__":
    print("Demonstrating large math functions:")
    num_factorial = 20
    print(f"Factorial of {num_factorial}: {large_factorial(num_factorial)}")

    base_power = 2
    exponent_power = 100
    print(f"{base_power} raised to the power of {exponent_power}: {large_power(base_power, exponent_power)}")

    num_prime = 1000000007
    print(f"Is {num_prime} prime? {is_prime_large(num_prime)}")

    n_fibonacci = 50
    print(f"The {n_fibonacci}th Fibonacci number: {fibonacci_large(n_fibonacci)}")

    n_combinations = 30
    k_combinations = 15
    print(f"Combinations of {k_combinations} from {n_combinations}: {combinations_large(n_combinations, k_combinations)}")
