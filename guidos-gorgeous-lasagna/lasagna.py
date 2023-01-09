"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language: https://en.wikipedia.org/wiki/Guido_van_Rossum
"""

# TODO: define the 'EXPECTED_BAKE_TIME' constant
# TODO: consider defining the 'PREPARATION_TIME' constant
#       equal to the time it takes to prepare a single layer


# TODO: define the 'bake_time_remaining()' function
def bake_time_remaining():
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    EXPECTED_BAKE_TIME = 40
    
    bake_time_remaining(elapsed_bake_time=30)
    return EXPECTED_BAKE_TIME - elapsed_bake_time

    """
        This function is used to calculate the remaining time, by subtracting the time already used in baking from the expected time
    """
    def preparation_time_in_minutes(number_of_layers):
        TIME_TAKEN_PER_LAYER = 2
    return TIME_TAKEN_PER_LAYER * number_of_layers
    """
    This function is used to calculate the preparation time used according to the number of layers the lasagna has , this is done by multiplying the number of layers
    and the time it takes per layer
    """
    
    def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
        return preparation_time_in_minutes + elapsed_bake_time
    """
        Return elapsed cooking time.
        This function takes two numbers which are the number of layers and the          time that has already been used during baking and calculates the tot            al elapsed minutes elapsed during cooking
    """


# TODO: define the 'preparation_time_in_minutes()' function
#       and consider using 'PREPARATION_TIME' here


# TODO: define the 'elapsed_time_in_minutes()' function
