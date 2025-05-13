# Ask the user for the filename to read
input_file = input("Enter the name of the file to read (with full path): ").strip()

try:
    # Try to open and read the file
    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()
    print("File read successfully!")

    # Modify the content (example: make everything uppercase)
    modified_content = content.upper()

    # Create a new file name
    output_file = input_file.replace(".txt", "_modified.txt")

    # Write the modified content to a new file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(modified_content)
    print(f"Modified content written to: {output_file}")

except FileNotFoundError:
    print("❌ Error: The file was not found. Please check the file path.")
except PermissionError:
    print("❌ Error: You don’t have permission to read this file.")
except Exception as e:
    print(f"❌ Unexpected error: {e}")