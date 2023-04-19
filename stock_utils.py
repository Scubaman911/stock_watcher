"""
Data utilities for the stock data models.
"""

def percentage_change(current_value: float, previous_value: float):
    x = (current_value - previous_value) / previous_value
    x_as_pcnt = x * 100
    return x_as_pcnt