from fib import fibonacci

# Test cases for the fibonacci function

def test_zeroth_fibonacci():
    assert(fibonacci(0) == 0)

def test_first_fibonacci():
    assert(fibonacci(1) == 1)

def test_21st_fibonacci():
    assert(fibonacci(21) == 10946)

def test_negative_fibonacci():
    assert(fibonacci(-1) == None)
