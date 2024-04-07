import autoflake
import autopep8
import sys

def fix_python_file(file_path):
    with open(file_path, 'r') as file:
        code = file.read()

    # Fix import statements
    fixed_code = autoflake.fix_code(code)

    # Fix syntax errors
    try:
        fixed_code = autopep8.fix_code(fixed_code)
    except Exception as e:
        print(f"Error fixing syntax: {e}")

    # Write the corrected code back to the file
    with open(file_path, 'w') as file:
        file.write(fixed_code)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python autocorrect.py <file_path>")
        sys.exit(1)

    file_path = sys.argv[1]
    fix_python_file(file_path)
    print(f"File '{file_path}' has been auto-corrected.")
