import app.io.input as input
import app.io.output as output
from pathlib import Path

def main():
    input_from_console = input.input_from_console()
    output.output_to_console(input_from_console)

    file_path_txt = 'data/input_file.txt'
    file_path_csv = 'data/input_file.csv'

    input_from_file = input.input_from_file(file_path_txt)
    output.output_to_console(input_from_file)

    input_with_pandas = input.input_with_pandas(file_path_csv)
    output.output_to_console(input_with_pandas)


if __name__ == '__main__':
    main()
