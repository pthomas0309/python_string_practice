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

# f-string syntax for Python 3.5 and earlier
# full_name = "{} {}".format(first_name. last_namei8)

# Output - hermoine granger
print(full_name)

# Output - Hello, Hermoine Granger!
print(f"Hello, {full_name.title()}!")

# Make the greeting its own variable
greeting = f"Hello, {full_name.title()}!"

# Output - Hello, Hermoine Granger!
print(greeting)

# Whitespace: Tabs and Newlines

# \t denotes a tab
# Output -      Python
print("\tPython")

# \n denotes a newline
# Output - 
# Desserts:
# Creme Brulee
# Chocolate Lava Cake
# Sugar Doughnuts
print("Desserts:\nCreme Brulee\nChocolate Lava Cake\nSugar Doughnuts")

# Output - 
# Desserts:
#   Creme Brulee
#   Chocolate Lava Cake
#   Sugar Doughnuts
print("Desserts:\n\tCreme Brulee\n\tChocolate Lava Cake\n\tSugar Doughnuts")

favorite_language = "  python "

# rstrip method removes whitespace from the right side of the string
# Output - "  python"
print(favorite_language.rstrip())

# lstrip method removes whitespace from the left side of the string
# Output - "python "
print(favorite_language.lstrip())

# strip method removes whitespace from both sides of the string
# Output - "python"
print(favorite_language.strip())