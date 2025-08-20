def main():
    # Define 3 helper functions for text-to-bytes conversion, bytes-to-text conversion, and byte reversal
    def reverse_bytes(bytes_data):
        return bytes_data[:: -1]

    def convert_bytes_to_text(bytes_data):
        return bytes_data.decode('utf-8').strip()

    def convert_text_to_bytes(bytes_data):
        return bytes_data.encode().hex()

    # Main program logic
    # Open the binary file for reading and create output text and bytes files for writing using the context manager
    try:
        with open('./data.bin', 'rb') as bin_file, \
                open("./converted.txt", 'w') as converted_text_file, \
                open("./reversed_bytes.txt", 'wb') as reversed_bytes_file:
            bin_data = bin_file.readlines()
            # Iterate through each line in the binary file
            for line in bin_data:
                # Decode the line to Unicode string and remove leading/trailing whitespaces
                unicode_line = convert_bytes_to_text(line)

                # Check if the line starts with "TEXT:"
                if unicode_line.startswith('TEXT:'):
                    text = unicode_line[len('TEXT:'):].upper() + "\n"
                    converted_text_file.write(text)

                # Check if the line starts with "BYTES:"
                elif unicode_line.startswith('BYTES:'):
                    # Extract the string and encode to hexadecimal
                    line_string = convert_text_to_bytes(unicode_line[:len('BYTES:')])
                    # Extract byte content, convert to bytes object(using fromhex()),
                    line_bytes = convert_text_to_bytes(unicode_line[len('BYTES:'):])
                    line_bytes_object = bytes.fromhex(line_bytes)
                    # converted_text_file.write(line_bytes_object)
                    # reverse bytes, and write to bytes file
                    reverse_line_bytes = reverse_bytes(line_bytes_object)
                    reversed_bytes_file.write(reverse_line_bytes)
            print("complete")

    except IOError as binary_error_msg:
            # Print success message
            print(binary_error_msg)
    # Handle file I/O errors
    # IOError - see definition, also Documentation: https://docs.python.org/3/library/io.html#

    # Handle other exceptions using the exception class


if __name__ == "__main__":
    main()
