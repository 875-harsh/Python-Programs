# Input: Name from the user
name = input("Enter your name: ")

# Reverse the name
reversed_name = name[::-1]

# Get the last 5 characters of the reversed name
last_five_characters = reversed_name[:5]

# Output the result
print(f"The reversed name is: {reversed_name}")
print(f"The last 5 characters of the reversed name are: {last_five_characters}")

