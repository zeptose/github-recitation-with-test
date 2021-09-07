
"""
Fibonacci number generator
When given a position, the function returns the fibonacci at that position in the sequence.
The first number in the fibonacci sequence is 0.
"""
def fibonacci(position):
  if(position == 2 or position == 3):
    return 1
  return fibonacci(position - 1) + fibonacci(position - 2)


# Test cases
print("The 2nd Fibonacci number: ", fibonacci(2))
print("The 21st Fibonacci number: ", fibonacci(21))
print("The 1st Fibonacci number: ", fibonacci(1))
print("The 0th Fibonacci number: ", fibonacci(0))

print("Code ran successfully!")


