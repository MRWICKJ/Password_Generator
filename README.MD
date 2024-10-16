# Password Generator

![Password Generator](path/to/your/image.png) <!-- Optional: Add an image here -->

A simple yet powerful password generator application built with Python. This tool allows users to create secure passwords with customizable options, using Tkinter for the graphical user interface and `pyperclip` for clipboard functionality.

## Features

- **Customizable Password Length**: Specify the desired length of the generated password.
- **Character Type Options**: Choose to include:
  - Uppercase and lowercase letters
  - Numbers
  - Special symbols
- **Clipboard Support**: Easily copy the generated password to the clipboard with a single click.
- **User-Friendly Interface**: Simple and intuitive GUI using Tkinter.
- **Command-Line Interface**: Generate passwords directly from the terminal.

## Requirements

- Python 3.9 or higher
- Tkinter (included with standard Python installations)
- `pyperclip`

## Installation

Follow these steps to set up the project locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/password-generator.git
   cd password-generator
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python -m venv venv
   ```

   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the GUI

To run the application with the graphical user interface, execute the following command:

```bash
python -m app.gui
```



### Running the CLI

To use the command-line interface, run the following command in your terminal:

```bash
python -m app.cli
```

You will be prompted to enter the following options:

1. **Password Length**: Enter the desired length for your password (default is 10).
2. **Include Letters**: Type `y` to include letters or `n` to exclude them.
3. **Include Numbers**: Type `y` to include numbers or `n` to exclude them.
4. **Include Symbols**: Type `y` to include symbols or `n` to exclude them.
5. **Copy to Clipboard**: After generating the password, you can choose to copy it to your clipboard by pressing Enter when prompted.

### Example CLI Interaction

```
Enter password length (default = 10): 12
Include letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y
Generated Password: Abc123!@#
Press Enter to Copy the Password (or any key to skip):
Password Copied Successfully!!
Press 'e' to Exit or any other key to continue:
```

## Example

Below is an example of what the application interface looks like:

![Password Generator Interface](path/to/your/image.png) <!-- Optional: Replace with an actual screenshot of your app -->

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

## Contributing

Contributions are welcome! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a Pull Request.

## Contact

For any inquiries, please reach out via:
- Email: your.email@example.com
- GitHub: [yourusername](https://github.com/yourusername)

---
