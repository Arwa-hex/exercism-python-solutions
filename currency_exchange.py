"""
This module provides functions to perform various currency exchange calculations,
including converting amounts, determining the number of bills, and handling exchange rates with spreads.
"""

def exchange_money(budget, exchange_rate):
    """
    Estimate the value of exchanged currency based on the given budget and exchange rate.

    :param budget: The amount of domestic currency to be exchanged.
    :param exchange_rate: The rate at which domestic currency is exchanged for foreign currency.
    :return: The amount of foreign currency after exchange.
    """
    return budget / exchange_rate

def get_change(budget, exchanging_value):
    """
    Calculate the amount of money left after exchanging a portion of the budget.

    :param budget: The total budget before exchange.
    :param exchanging_value: The amount of money to be exchanged from the budget.
    :return: The remaining money after exchange.
    """
    return budget - exchanging_value

def get_value_of_bills(denomination, number_of_bills):
    """
    Calculate the total value of a given number of bills.

    :param denomination: The value of a single bill.
    :param number_of_bills: The total number of bills.
    :return: The total value of the bills.
    """
    return denomination * number_of_bills

def get_number_of_bills(amount, denomination):
    """
    Determine how many whole bills can be obtained from a given amount.

    :param amount: The total amount of money available.
    :param denomination: The value of a single bill.
    :return: The number of whole bills that can be obtained.
    """
    return amount // denomination

def get_leftover_of_bills(amount, denomination):
    """
    Calculate the leftover amount after converting a given amount into bills.

    :param amount: The total amount of money available.
    :param denomination: The value of a single bill.
    :return: The leftover amount after obtaining whole bills.
    """
    return amount % denomination

def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculate the maximum exchangeable value after applying an exchange rate with a spread,
    and rounding down to the nearest denomination of bills.

    :param budget: The amount of domestic currency available for exchange.
    :param exchange_rate: The base exchange rate without the spread.
    :param spread: The percentage fee (spread) applied to the exchange rate.
    :param denomination: The value of a single bill in the foreign currency.
    :return: The maximum value in foreign currency that can be exchanged into whole bills.
    """
    effective_rate = exchange_rate * (1 + spread / 100)
    exchanged_amount = budget / effective_rate
    number_of_bills = exchanged_amount // denomination
    return int(number_of_bills * denomination)
