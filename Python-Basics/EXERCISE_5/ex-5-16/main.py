from file_open import FileOpen

with FileOpen("test.txt", "w") as file:
    file.write("Hello, Context Manager!")

print("File written successfully.")
