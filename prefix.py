import os
import re

def extract_addresses(prefix):
    # Regular expression pattern to match addresses
    pattern = r'PubAddress:\s+(' + prefix + r'\w+)'

    # List to store the extracted addresses
    addresses = []

    # Get the current directory
    current_dir = os.getcwd()

    # Iterate over each text file in the folder
    for file_name in os.listdir(current_dir):
        if file_name.endswith('.txt'):
            file_path = os.path.join(current_dir, file_name)
            with open(file_path, 'r') as file:
                # Read the entire content of the file
                content = file.read()
                # Search for addresses with the specified prefix
                matches = re.findall(pattern, content)
                addresses.extend(matches)

    # Write the addresses to a text file
    output_file = prefix + '_output.txt'
    with open(output_file, 'w') as file:
        for address in addresses:
            file.write(address + '\n')

    print(f"Addresses with prefix '{prefix}' extracted from all files and saved to '{output_file}'.")

# Prompt for the prefix
prefix = input("Enter the prefix to search for: ")

# Call the function to extract addresses
extract_addresses(prefix)
