def get_factorial(num):
    """Returns the factorial of a number using a for loop."""
    if num < 0:
        return None  
    
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

def sum_odd_numbers(num):
    """Returns the sum of odd numbers up to a given number using a while loop."""
    total = 0
    current = 1
    
    while current <= num:
        total += current  # Add current odd number
        current += 2  # Move to the next odd number
    
    return total

