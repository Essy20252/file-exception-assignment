# file_handler.py

def modify_content(content):
    # Example: Convert text to uppercase
    return content.upper()

def main():
    try:
        # Ask the user for the input filename
        input_filename = input("Enter the name of the file to read from: ")
        
        # Try to open and read the file
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content
        modified = modify_content(content)

        # Write to a new file
        output_filename = "modified_" + input_filename
        with open(output_filename, 'w') as outfile:
            outfile.write(modified)

        print(f"Modified content written to: {output_filename}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename.")
    except PermissionError:
        print("Error: You don't have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
