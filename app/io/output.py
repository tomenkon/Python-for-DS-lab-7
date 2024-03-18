def output_to_console(text):
    """
    Output text to console

    Args:
        text (str): Text to be output
    """
    print(text)


def output_to_file(text, file_path):
    """
    Write text to a txt file

    Args:
        text (str): Text to write to file
        file_path (str): Path to the out file
    """
    try:
        with open(file_path, 'w') as file:
            file.write(text)
    except FileNotFoundError:
        print(f'Cant write to file {file_path}')