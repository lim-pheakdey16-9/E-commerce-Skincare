# myapp/utils.py

def format_name(first_name, last_name):
    """
    Formats a full name with a specific style.
    """
    return f"{first_name.capitalize()} {last_name.capitalize()}"

def calculate_discount(price, discount_percentage):
    """
    Calculates the discounted price.
    """
    discount_amount = price * (discount_percentage / 100)
    return price - discount_amount