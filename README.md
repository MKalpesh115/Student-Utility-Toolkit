# Student Utility Toolkit

Student Utility Toolkit is a beginner-friendly, menu-driven Python command-line application with handy tools for everyday calculations and text tasks.

## Features

- **Calculator:** Add, subtract, multiply, and divide two numbers. Division by zero is handled safely.
- **Temperature Converter:** Convert Celsius to Fahrenheit or Fahrenheit to Celsius.
- **Word Counter:** Count the words and characters in a sentence. Character counts include spaces.
- **Password Generator:** Generate a random password of a chosen length containing letters, numbers, and special characters.
- **Input validation:** Invalid menu choices and numeric inputs are handled with clear messages.

## Requirements

- Python 3.7 or newer
- No external packages are required. The application uses only Python's standard library.

## Installation

1. Download or clone this project and open the `Student-Utility-Toolkit` folder in Visual Studio Code.
2. Confirm Python is installed by opening the VS Code terminal (**Terminal > New Terminal**) and running:

   ```bash
   python --version
   ```

   On some systems, use `py --version` instead.

## Run the application

In the VS Code terminal, from the project folder, run:

```bash
python main.py
```

On Windows, if `python` is not recognized, try:

```bash
py main.py
```

Choose an option from the menu and follow the prompts. Select **5** to exit.

## Project files

- `main.py` — application and menu
- `requirements.txt` — dependency information (no external packages)
- `.gitignore` — common Python-generated files excluded from version control
