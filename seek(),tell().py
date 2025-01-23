# The seek function allows you to move the current position within a file to a specific point. The position is specified in bytes, and you can move either forward or backward from the current position. For example:

with open( 'file.txt', 'r') as f:
    print(type(f))
# Move to the 10th byte in the file
    f.seek(10)
# Read the next 5 bytes
    data = f. read (5)
    print(data)


# tellO function
# The tellO function returns the current position within the file, in bytes.
# This can be useful for keeping track of your location within the file or for seeking to a specific position relative to the current position.

with open( 'file.txt', 'r') as f:
# Read the first 10 bytes
    data = f. read (10)
# Save the current position
    current_position = f.tell()
# Seek to the saved position
    f. seek(current_position)