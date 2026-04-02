def remove_comments(line):
    in_single = False
    in_double = False
    result = ""

    i = 0
    while i < len(line):
        if line[i] == "'" and not in_double:
            in_single = not in_single
        elif line[i] == '"' and not in_single:
            in_double = not in_double
        elif line[i] == '#' and not in_single and not in_double:
            break
        result += line[i]
        i += 1

    return result.rstrip()


source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

try:
    with open(source, 'r') as src, open(destination, 'w') as dest:
        for line in src:
            clean_line = remove_comments(line)
            if clean_line.strip() != "":
                dest.write(clean_line + '\n')

    print("\n--- Source File Content ---")
    with open(source, 'r') as src:
        print(src.read())

    print("\n--- Destination File Content (Without Comments) ---")
    with open(destination, 'r') as dest:
        print(dest.read())

except FileNotFoundError:
    print("Error: Source file not found.")
except Exception as e:
    print("Error:", e)
