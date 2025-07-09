user_input = input("Enter some text to write to the file: ")

with open("sample.txt", "w") as file:
    file.write(user_input + "\n")

# Step 2: Append additional data
additional_input = input("Enter additional text to append to the file: ")

with open("sample.txt", "a") as file:
    file.write(additional_input + "\n")

# Step 3: Read and display final content
print("\nFinal content of 'sample.txt':")
with open("sample.txt", "r") as file:
    for line_number, line in enumerate(file, start=1):
        print(f"Line {line_number}: {line.strip()}")