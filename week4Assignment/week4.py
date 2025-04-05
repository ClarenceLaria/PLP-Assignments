# File Read & Write Challenge

filename = input("Enter the filename you want to read: ")
# Step 1: Read content from an existing file
try:
    with open(filename, "r") as file:
        content = file.read()  # Reading the entire content of the file
        print("File content read successfully:", content)

    # Step 2: Modify the content (e.g., convert text to uppercase)
    modified_content = content.upper()  # Example modification: converting to uppercase

    # Step 3: Write the modified content to a new file
    with open("output.txt", "w") as new_file:
        new_file.write(modified_content)  # Writing the modified content to output.txt

    print("File has been successfully read, modified, and saved to output.txt")

except FileNotFoundError:
    print(f"The file '{filename}' does not exist.")
except IOError:
    print("There was an error reading or writing to the file.")
