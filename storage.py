import os

# Define the file path
file_path1 = "3GB_file.bin"

# Define the size of the file in bytes (1 GB = 1024^3 bytes)
file_size = 3 * 1024 * 1024 * 1024  # 1 GB in bytes
for i in range (1,10):
  # Open the file in write mode
  file_path = file_path1 + str(i)
  with open(file_path, "wb") as f:
      # Write random data until the file size reaches 1 GB
      f.write(os.urandom(file_size))

print(f"File '{file_path}' of size 3 GB created successfully.")
