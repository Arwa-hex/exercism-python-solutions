"""Guido's Gorgeous Lasagna

This module provides functions to calculate the preparation time, remaining baking time, 
and total elapsed cooking time for a lasagna recipe.
"""

# Constants
EXPECTED_BAKE_TIME = 40  # Define expected bake time in minutes

def bake_time_remaining(actual_bake_time):
    """Calculate the remaining bake time for the lasagna.

    :param actual_bake_time: int - the number of minutes the lasagna has been baking.
    :return: int - remaining bake time (in minutes) needed.

    This function takes the elapsed baking time as an argument and returns the number of minutes 
    the lasagna still needs to bake based on the expected bake time.
    """
    return EXPECTED_BAKE_TIME - actual_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculate the preparation time for the lasagna.

    :param number_of_layers: int - the number of layers in the lasagna.
    :return: int - total preparation time (in minutes) for the given layers.

    This function takes an integer representing the number of layers added to the lasagna 
    and calculates the total preparation time, assuming each layer takes 2 minutes to prepare.
    """
    return number_of_layers * 2

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.

    :param number_of_layers: int - the number of layers in the lasagna.
    :param elapsed_bake_time: int - elapsed cooking time.
    :return: int - total time elapsed (in minutes) preparing and cooking.

    This function takes two integers representing the number of lasagna layers and the
    time already spent baking and calculates the total elapsed minutes spent cooking the
    lasagna.
    """
    preparation_time = preparation_time_in_minutes(number_of_layers)
    total_time = preparation_time + elapsed_bake_time
    return total_time

# Example usage
if __name__ == "__main__":
    try:
        layers = int(input("Enter the number of layers: "))
        elapsed_bake = int(input("Enter the elapsed bake time in minutes: "))

        if layers < 0 or elapsed_bake < 0:
            raise ValueError("Number of layers and elapsed bake time must be non-negative.")

        prep_time = preparation_time_in_minutes(layers)
        remaining_bake_time = bake_time_remaining(elapsed_bake)
        total_elapsed_time = elapsed_time_in_minutes(layers, elapsed_bake)

        print(f"Preparation time for {layers} layers: {prep_time} minutes")  
        print(f"Remaining bake time: {remaining_bake_time} minutes")         
        print(f"Total elapsed time: {total_elapsed_time} minutes")           

    except ValueError as e:
        print(f"Invalid input: {e}")
