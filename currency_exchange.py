# 1. Calculate the value after exchange
def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

# 2. Calculate the amount of money left after exchanging part of the budget
def get_change(budget, exchanging_value):
    return budget - exchanging_value

# 3. Calculate the total value of bills based on denomination and the number of bills
def get_value_of_bills(denomination, number_of_bills):
    return denomination * number_of_bills

# 4. Calculate the number of whole bills that fit into the amount
def get_number_of_bills(amount, denomination):
    return amount // denomination

# 5. Calculate the leftover money after fitting bills into the amount
def get_leftover_of_bills(amount, denomination):
    return amount % denomination

# 6. Calculate the maximum exchangeable value after applying spread and converting to denomination
def exchangeable_value(budget, exchange_rate, spread, denomination):
    # Adjust the exchange rate to account for the spread
    adjusted_rate = exchange_rate * (1 + spread / 100)
    
    # Calculate the total value in the foreign currency
    total_value = budget / adjusted_rate
    
    # Calculate the number of whole bills that can be obtained
    number_of_bills = total_value // denomination
    
    # Return the value in terms of whole bills
    return int(number_of_bills * denomination)

# Example Test Cases
print(exchange_money(127.5, 1.2))            # Output: 106.25
print(get_change(127.5, 120))                # Output: 7.5
print(get_value_of_bills(5, 128))            # Output: 640
print(get_number_of_bills(127.5, 5))         # Output: 25
print(get_leftover_of_bills(127.5, 20))      # Output: 7.5
print(exchangeable_value(127.25, 1.20, 10, 20))  # Output: 80
print(exchangeable_value(127.25, 1.20, 10, 5))   # Output: 95
