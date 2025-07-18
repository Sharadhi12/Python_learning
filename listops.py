# Task 2: Demonstrate List Slicing

# Step 1: Create a list of numbers from 1 to 10
numbers = list(range(1, 11))

# Step 2: Extract the first five elements
first_five = numbers[:5]

# Step 3: Reverse these extracted elements
reversed_five = first_five[::-1]

# Step 4: Print both the extracted list and the reversed list
print("Original list:", numbers)
print("First five elements:", first_five)
print("Reversed first five elements:", reversed_five)
