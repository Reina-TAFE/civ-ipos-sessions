def main():
    # Phase 1: File Navigation
    with open("./data_v2.bin", 'rb') as file:
        data = file.read()
        # Navigate to the 5th byte position
        file.seek(4)
        # Read and print the next 4 bytes from the current position
        print(file.read(4).decode('utf-8'))

        # Move the file pointer to the beginning of the file
        file.seek(0)
        # Read and print the first 8 bytes from the file
        print(file.read(8))

        # Print the current file pointer position
        print(file.tell())

        # Use the find() method to search for the string "ABC" in the file
        print(data.find("ABC".encode()))




    # Re-open the data.bin file in binary write-append mode
    with open("./data_v2.bin", "ab") as file:
        data = file.read()
        # Use the tell() method to get the current file pointer position and store it as a bookmark
        pointer = file.tell()

        # Write the string "XYZ" to the file
        file.write("XYZ".encode())

        # Use the bookmarked pointer position to append the string "123" to the file
        file.seek(pointer)
        file.write("123".encode())
    # create three non naked exception handlers for: 
    # not finding the file, i/o error & all other exceptions


if __name__ == "__main__":
    main()
