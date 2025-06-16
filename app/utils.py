def add_commission(number: float) -> float:
    """Adds a standard commission of 1 to a numeric string and returns the result as a string.
        Examples:
            >>> add_commission(100)
            '101.0'
            >>> add_commission(68.9879)
            '69.9879'
        """
    try:
        return number + 1
    except ValueError:
        raise ValueError("Input must be a numeric string")
