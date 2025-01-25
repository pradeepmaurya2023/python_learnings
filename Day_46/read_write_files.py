import os

# Open the file in write-only mode
f = os.open("myfile.txt", os.O_RDONLY)

contents = os.read(f,10)

print(contents)

# Write to the file
# os.write(f, b"Hello, world!")

# Close the file
os.close(f)