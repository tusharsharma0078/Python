from pathlib import Path

print("Script location:", Path(__file__).parent)

file_path = Path(__file__).parent / "demo2_file.txt"

with open(file_path, "w") as file:
    file.write("Hello Tushar")

print("File created:", file_path)
print("Exists:", file_path.exists())