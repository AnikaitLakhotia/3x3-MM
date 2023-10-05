def reverse_map(sat_assignment, cumulative_dict):
    """
    Reverse map the values in the SAT assignment's variables to their corresponding keys(string form) in
    cumulative_dict and their respective assignments to {1,0}.

    Args:
        sat_assignment (str): A space-separated string that is the output of the SAT Solver
                              if the instance given to it is satisfiable.
        cumulative_dict (dict): A dict containing all the variables in the encoding(as keys) and their
                                corresponding unique integer values.

    Returns:
        dict: A dictionary mapping keys of cumulative_dict to 1 or 0 based on the signs of
              their respective integer values in sat_assignment.(0 is sign is '-' and 1 otherwise)
    """

    number_list = sat_assignment.split()
    result_dict = {}
    for number in number_list:
        if number.startswith("-"):
            number = number[1:]
            for key, value in cumulative_dict.items():
                if int(number) == value:
                    result_dict[key] = 0
        else:
            for key, value in cumulative_dict.items():
                if int(number) == value:
                    result_dict[key] = 1
    return result_dict


def verifier(sat_assignment, cumulative_dict, num_t):
    """
    Verify if the sat_assignment obeys the rules of the Brent equations.

    Args:
        sat_assignment (str): A space-separated string of values.
        cumulative_dict (dict): A dictionary mapping keys to values.
        num_t (int): Number of 't's in each Brent equation.

    Returns:
        int: 1 if the condition is satisfied, 0 otherwise.
    """

    result = reverse_map(sat_assignment, cumulative_dict)
    for key, value in result.items():
        if key.startswith(f"t_1"):
            sum_val = 0
            val_t, val_1, val_2, val_3, val_4, val_5, val_6 = key.split("_")[1:]
            for i in range(1, num_t + 1):
                sum_val += result[f't_{i}_{val_1}_{val_2}_{val_3}_{val_4}_{val_5}_{val_6}']
            if val_2 == val_3 and val_1 == val_5 and val_4 == val_6 and sum_val % 2 == 0:
                return 0
            elif (val_2 != val_3 or val_1 != val_5 or val_4 != val_6) and sum_val % 2 != 0:
                return 0
            else:
                return 1