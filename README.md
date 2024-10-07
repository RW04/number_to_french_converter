## Project Structure

```bash
number_to_french_converter/
│
├── app.py                    # Gradio app interface
├── main.py                   # Main entry point (command line interface)
├── README.md                 # Documentation
├── requirements.txt          # Dependencies (Gradio, etc.)
├── src/                      # Source code folder
│   ├── converter.py          # Main logic for number-to-French conversion
│   └── __init__.py           # Makes src a package
├── tests/                    # Unit tests folder
│   ├── test_converter.py     # Unit tests for NumberToFrenchConverter class
│   └── __init__.py           # Makes tests a package
├── logs/                     # Logs folder
│   └── converter.log         # Logs will be saved here
└── utils/                    # Utility functions (if needed)
    └── __init__.py           # Utils package (optional)
```


## Installation

1.Clone the repository:

```bash
git clone https://github.com/yourusername/number_to_french_converter.git
cd number_to_french_converter
```

2.Install the required dependencies:

```bash
pip install -r requirements.txt
```


## Usage

**Running the Command-Line Interface (CLI)**
You can convert numbers directly from the terminal by running `main.py`:

```bash
python main.py 10 25 68 99
```

This will output the French word equivalents of the numbers provided.

**Running the Gradio GUI**
To use the graphical interface, simply run the `app.py`:

```bash
python app.py
```

This will launch the Gradio interface in your browser, where you can input numbers and get their French word equivalents.


## Logging

Logs for the conversion process are saved in the logs/converter.log file. You can check this file to see detailed logging information, which includes which numbers are being converted and any errors that might occur.


## Running Unit Tests
To run the unit tests, use the following command:

```bash
python -m unittest discover tests/
```

This will run all the unit tests in the `tests/` folder and provide feedback on the converter's correctness.


## Algorithm Concerns

- Decimal Numbers: This algorithm is designed for whole numbers only. It does not handle decimal numbers, fractions, or other non-integer inputs.

- Numbers Greater Than 999,999: The current implementation handles numbers up to 999,999. If you attempt to convert a number larger than this, the program will raise a `ValueError` stating that the number is too large to convert.

- Negative Numbers: Negative numbers are not supported in this version. Any negative number will raise an error.

