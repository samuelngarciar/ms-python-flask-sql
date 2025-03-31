def validate_input(input_data):
    if not isinstance(input_data, int) or input_data < 0:
        raise ValueError("Invalid input")
