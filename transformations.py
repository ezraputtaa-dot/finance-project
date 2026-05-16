print ("hello print")


def transform_data(data):
    # Example transformation: Convert all values to uppercase
    transformed_data = {key: value.upper() for key, value in data.items()}
    return transformed_data