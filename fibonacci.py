import time

# Non-Recursive Fibonacci
def fib_non_recursive(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

# Recursive Fibonacci
def fib_recursive(n):
    if n <= 1:
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

def fib_recursive_sequence(n):
    return [fib_recursive(i) for i in range(n)]

# Example
n = int(input("Enter n: "))

# Non-Recursive
start = time.time()
seq1 = fib_non_recursive(n)
end = time.time()
print("Non-Recursive Fibonacci Sequence:", seq1)
print("Time Taken:", round(end - start, 6), "seconds")
print("Time Complexity: O(n), Space Complexity: O(1)\n")

# Recursive
start = time.time()
seq2 = fib_recursive_sequence(n)
end = time.time()
print("Recursive Fibonacci Sequence:", seq2)
print("Time Taken:", round(end - start, 6), "seconds")
print("Time Complexity: O(2^n), Space Complexity: O(n)")

