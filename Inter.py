# Input: Two strings from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Initialize the result string
result = ""

# Determine the length of the shorter string
min_length = min(len(string1), len(string2))

# Interleave characters from both strings
for i in range(min_length):
    result += string1[i] + string2[i]

# Add the remaining characters from the longer string
result += string1[min_length:] + string2[min_length:]

# Output the result
print(f"The interleaved result is: {result}")


