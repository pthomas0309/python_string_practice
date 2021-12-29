# String practice file 

name = "preston thomas"

# title method changes each word to title case .
# Output - Preston Thomas
print(name.title())

# upper method changes the string to be full uppercase.
# Output - PRESTON THOMAS
print(name.upper())

# lower method changes the string to be all lowercase.
# Output - preston thomas
print(name.lower())

# String Concatonation

first_name = "hermoine"

last_name = "granger"

# f-string formats string by replacing variable names in braces
# with the value of the variable.
full_name = f"{first_name} {last_name}"

# Output - hermoine granger
print(full_name)

# Output - Hello, Hermoine Granger
print(f"Hello, {full_name.title()}!")