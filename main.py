import sys
from src.converter import NumberToFrenchConverter

def main():
    numbers = [int(x) for x in sys.argv[1:]]
    converter = NumberToFrenchConverter()
    french_numbers = [converter.convert(number) for number in numbers]
    for number, french in zip(numbers, french_numbers):
        print(f"{number} in French is: {french}")

if __name__ == "__main__":
    main()
