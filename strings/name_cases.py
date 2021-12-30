# Personal exercises

# Create a variable to represent a persons name
name = "Mr. Anderson"

# Then print a message using the name variable
# Output - You hear that Mr. Anderson? That is the sound of inevitability!
print(f"You hear that {name}? That is the sound of inevitability!")

# Create a variable representing a name
name = "bellatrix lestrange"

# Display the name in title case,
# Output - Bellatrix Lestrange
print(name.title())

# upper case,
# Output - BELLATRIX LESTRANGE
print(name.upper())

# and lower case
# Output - bellatrix lestrange
print(name.lower())

# Find a quote and print the quote as well as the name of its author
# Output - "If you want to find the secrets of the universe, think in terms of energy, frequency and vibration." - Nikola Tesla
print("\"If you want to find the secrets of the universe, think in terms of energy, frequency and vibration.\" - Nikola Tesla")

# Create a variable with the value of the author's name
famous_person = "Nikola Tesla"

# Create a variable with the value of the message, including the name of the author
message =  f"\"If you want to find the secrets of the universe, think in terms of energy, frequency and vibration.\" - {famous_person}"

# Output - "If you want to find the secrets of the universe, think in terms of energy, frequency and vibration." - Nikola Tesla
print(message)

# Remove whitespace around the string variable name
name = "\tRose\nTyler\t"

# Output - "    Rose
# Tyler    "
print(name)

# Strip the whitespace on the left side of the string
# Output - "Rose
# Tyler    "
print(name.lstrip())

# Strip whitespace from the right side of the string
# Output - "    Rose
# Tyler"
print(name.rstrip())

# Strip whitespace from both sides of the string
# Output - "Rose
# Tyler"
print(name.strip())