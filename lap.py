# Problem: Write a Python function fibonacci(n) that returns the n-th number in the Fibonacci sequence. The Fibonacci sequence is defined as:

# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2) for n > 1

def fibonacci(n):
    """Return the n-th number in the Fibonacci sequence using iteration."""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# Example usage:
print(fibonacci(5))  # Output: 5
print(fibonacci(10)) # Output: 55
