import hashlib

# Prompt the user for the input filename containing passwords
input_file = input("Enter the name of the input password file (e.g., 'passwords.txt'): ")

# Read in the list of passwords from the input text file
try:
    with open(input_file, 'r') as f:
        passwords = f.read().splitlines()
except FileNotFoundError:
    print(f"Error: The input file '{input_file}' was not found.")
    exit(1)

# Compute the SHA1 hash for each password
hashes = [hashlib.sha1(password.encode()).hexdigest() for password in passwords]

# Prompt the user for the output filename for hash values
output_file = input("Enter the name of the output hash file (e.g., 'password_hashes.txt'): ")

# Save the hash values to the output text file
with open(output_file, 'w') as f:
    for hash_hex in hashes:
        f.write(hash_hex + '\n')

print(f"{len(hashes)} hash values saved to {output_file}.")
