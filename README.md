# File Handling and Exception Handling Assignment 📂⚠️

## Description

This Python program demonstrates how to:
- Read content from a user-specified file.
- Modify that content (convert it to uppercase).
- Write the modified content to a new file.
- Handle errors such as:
  - File not found
  - Permission denied
  - Other unexpected exceptions

This assignment is part of the **Python Week 4 Module**.

## How It Works

1. The user is asked to enter the name of a file to read from.
2. The program tries to open and read that file.
3. If successful, the content is converted to **uppercase**.
4. The modified content is written to a **new file** (named `modified_filename.txt`).
5. If any errors occur, the program handles them gracefully using `try-except`.

## Files Included

- `file_handler.py`: Main Python script.
- `README.md`: Project description.
- *(Optional)* `sample.txt`: Test file with sample content.

## How to Run

Make sure you have Python installed. Then run the script from your terminal:

```bash
python file_handler.py
