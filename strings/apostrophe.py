# Proper way to include apostrophes in a string
message = "One of Python's strengths is its diverse community"

# also acceptable
message = 'One of Python\'s strengths is its diverse community'

# Output - One of Python's strengths is its diverse community
print(message)

# Improper inclusion of apostrophes
# message = 'One of Python's strengths is its diverse community'

# Output - 
# File "C:\Users\prest\python_files\python_variable_practice\strings\apostrophe.py", line 5
# message = 'One of Python's strengths is its diverse community'                                                       ^
# SyntaxError: unterminated string literal (detected at line 5)
# print(message)