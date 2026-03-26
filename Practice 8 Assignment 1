def convert_to_uppercase(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            content = file.read()

        upper_content = content.upper()

        with open(output_file, 'w') as file:
            file.write(upper_content)

        print("File converted to uppercase successfully.")

    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print("Error:", e)


input_file = "input.txt"
output_file = "output.txt"

convert_to_uppercase(input_file, output_file)
