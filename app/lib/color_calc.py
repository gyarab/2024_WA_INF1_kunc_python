from datetime import datetime, timedelta

def calculate_expiry_color(expiry_date: datetime) -> str:
    """
    Calculate the color of the expiry date based on the number of days left

    Args:
        expiry_date (datetime): the expiry date of the product

    Returns:
        str: hex color code
    """
    delta = expiry_date - datetime.now(expiry_date.tzinfo)

    days_left = delta.days
    if days_left >= 14:
        return "#00FF00"
    elif days_left <= 0:
        return "#FF0000"
    else:
        ratio = days_left / 14
        red = int(255 * (1 - ratio))
        green = int(255 * ratio)
        return f"#{red:02x}{green:02x}00"