import itertools

# Step 1: Choose a set of base words
base_words = []
while True:
    word = input("Enter a base word (or type 'done' to finish): ")
    if word.lower() == 'done':
        break
    base_words.append(word)

# Step 2: Define transformation options
transformations = {
    "Add numbers to the end": "numbers",
    "Add symbols to the end": "symbols",
    "Capitalize first letter": "capitalize",
    "Capitalize all letters": "uppercase",
    "Replace letters with similar-looking characters": "replace",
}

selected_transformations = []
print("\nSelect transformation options (separate by commas):")
for idx, (option, _) in enumerate(transformations.items(), start=1):
    print(f"{idx}. {option}")
options = input("Enter the numbers of the transformations you want (e.g., 1, 3, 5): ").split(',')
for option in options:
    selected_transformations.append(list(transformations.values())[int(option) - 1])

# Step 3: Combine variations of each base word
num_passwords = int(input("Enter the number of password combinations to generate: "))
variations = []

for word in base_words:
    for transform in selected_transformations:
        if transform == "numbers":
            for i in range(10):
                variations.append(word + str(i))
        elif transform == "symbols":
            for symbol in ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']:
                variations.append(word + symbol)
        elif transform == "capitalize":
            variations.append(word.capitalize())
        elif transform == "uppercase":
            variations.append(word.upper())
        elif transform == "replace":
            replacements = {'a': '@', 'e': '3', 'i': '1', 'o': '0', 's': '$'}
            for old, new in replacements.items():
                replaced_word = word.replace(old, new)
                if replaced_word != word:
                    variations.append(replaced_word)

passwords = list(set(itertools.permutations(variations, 3)))[:num_passwords]

# Step 4: Filter out weak passwords
strong_passwords = []
for password in passwords:
    password_str = ''.join(password)
    if len(password_str) >= 8 and len(set(password_str)) >= 6:
        strong_passwords.append(password_str)

# Step 5: Save passwords to a text file
output_file = input("Enter the filename to save strong passwords (e.g., 'passwords.txt'): ")
with open(output_file, 'w') as f:
    f.write('\n'.join(strong_passwords))

print(f"{len(strong_passwords)} strong passwords saved to {output_file}.")
