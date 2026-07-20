from pathlib import Path
import os

file_path = Path(__file__).parent / "demo2_file.txt"

if file_path.exists():
    os.remove(file_path)
    print("File deleted successfully.")
else:
    print("File does not exist.")