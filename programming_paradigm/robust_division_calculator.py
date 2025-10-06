def safe_divide(numerator, denominator):
    """
    Performs division with error handling for non-numeric input and division by zero.

    Args:
        numerator: The number to be divided (can be str or numeric).
        denominator: The number to divide by (can be str or numeric).

    Returns:
        A message string showing the result or describing the error.
    """
    try:
        num = float(numerator)
        den = float(denominator)

        if den == 0:
            return "Error: Cannot divide by zero."

        result = num / den
        return f"The result of the division is {result}"
    
    except ValueError:
        return "Error: Please enter numeric values only."
