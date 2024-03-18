import pandas as pd

def input_from_console():
    """
    Reads text from console

    Returns:
        str: Input text
    """
    return input("Enter your text:\n")


def input_from_file(file_path):
    """
    Reads a text file

    Args:
        file_path (str): Path to file

    Returns:
        str: File content
    """
    try:
        with open(file_path, 'r') as file:
            text = file.read()
        return text
    except FileNotFoundError:
        print(f"File {file_path} not found")


def input_with_pandas(file_path):
    """
    Reads the file using pandas

    Args:
        file_path (str): Path to file.

    Returns:
        pandas.DataFrame: DataFrame from file
    """
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"File {file_path} not found")