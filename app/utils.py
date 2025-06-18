def add_commission(commission: float, amount: float) -> float:
    try:
        return commission+amount
    except ValueError:
        raise ValueError("Input must be a float")
