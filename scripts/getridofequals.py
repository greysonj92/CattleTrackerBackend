import sys

def remove_equals(input_file, output_file):
    substring = "=="
    lines = []
    updated_lines = []
    with open(input_file, 'r') as my_file:
        lines = my_file.readlines()
    for line in lines:
        print(line)
        first = line.find(substring)
        second = line.find("==", first + len(substring))
        updated_lines.append(line[0:second] + "\n")
    with open(output_file, 'w') as my_file:
        my_file.writelines(updated_lines)

if __name__ == "__main__":
    remove_equals(sys.argv[1], sys.argv[2])