def create_var(num_t, num_row, num_col, shift, var_char):
    """
    Create all variables (e.g., "b_1_2_1", "b_6_2_3", etc.) starting with the same
    character ('a' for alpha, 'b' for beta, or 'g' for gamma) representing the respective variables in
    Brent equations and map them to unique integer values using a dictionary.

    Args:
        num_t (int): Number of 't's in each Brent equation.
        num_row (int): Number of rows in the corresponding matrix.
        num_col (int): Number of columns in the corresponding matrix.
        shift (int): Current variable index offset.
        var_char (str): The character to use for variable names.

    Returns:
        dict: Dictionary of custom 'var' variables and their corresponding unique integer values.

    Notes:
        1. The function must be run three times in total with 'a', 'b', and 'g'.
        2. The values corresponding to each variable will act as the variables in the CNF file.
        3. Shift is used to ensure the values are unique, not only in their dictionary but also with respect
           to values for other variables in the encoding.
    """

    var_dict = {}  # Initialize an empty dictionary to store variable mappings

    val_t_range = range(1, num_t + 1)  # Create a range for 't' values
    val_1_range = range(1, num_row + 1)  # Create a range for the first index
    val_2_range = range(1, num_col + 1)  # Create a range for the second index

    i = 1  # Initialize a counter for unique integer values
    for t in val_t_range:
        for val_1 in val_1_range:
            for val_2 in val_2_range:
                key = f"{var_char}_{t}_{val_1}_{val_2}"  # Construct the variable name
                var_dict[key] = shift + i  # Map the variable name to a unique integer value
                i += 1

    return var_dict  # Return the dictionary of variable mappings
