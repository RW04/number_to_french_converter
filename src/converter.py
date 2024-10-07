import logging

class NumberToFrenchConverter:
    """Convert numbers to their French word equivalents."""

    def __init__(self):
        self.units = {
            0: "zéro", 1: "un", 2: "deux", 3: "trois", 4: "quatre", 5: "cinq", 6: "six", 
            7: "sept", 8: "huit", 9: "neuf", 10: "dix", 11: "onze", 12: "douze", 
            13: "treize", 14: "quatorze", 15: "quinze", 16: "seize"
        }
        self.tens = {
            10: "dix", 20: "vingt", 30: "trente", 40: "quarante", 50: "cinquante", 
            60: "soixante", 80: "quatre-vingts"
        }
        logging.basicConfig(filename='logs/converter.log', level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def convert(self, n):
        """Main method to convert number to French words."""
        self.logger.info(f"Converting number: {n}")
        if n < 0:
            raise ValueError("Negative numbers are not supported.")
        if n < 17:
            return self.units[n]
        elif n < 100:
            return self._convert_tens(n)
        elif n < 1000:
            return self._convert_hundreds(n)
        elif n < 1000000:
            return self._convert_thousands(n)
        else:
            raise ValueError("Number too large to convert.")

    def _convert_tens(self, n):
        """Convert numbers between 17 and 99."""
        if n in self.tens:
            if n == 80:
                return "quatre-vingts"
            return self.tens[n]
        elif n < 70:
            ten = (n // 10) * 10
            unit = n % 10
            if unit == 1:
                return self.tens[ten] + "-et-un"
            else:
                return self.tens[ten] + "-" + self.units[unit]
        elif n < 80:
            return "soixante-" + self.convert(n - 60)
        else:
            unit = n % 20
            if unit == 0:
                return "quatre-vingts"
            elif unit == 1:
                return "quatre-vingt-un"
            else:
                return "quatre-vingt-" + self.convert(unit)

    def _convert_hundreds(self, n):
        """Convert numbers between 100 and 999."""
        hundred = n // 100
        remainder = n % 100
        if hundred == 1:
            result = "cent"
        else:
            result = self.units[hundred] + " cent"
        if remainder == 0 and hundred > 1:
            return result + "s"
        return result + " " + self.convert(remainder)

    def _convert_thousands(self, n):
        """Convert numbers between 1000 and 999999."""
        thousand = n // 1000
        remainder = n % 1000
        if thousand == 1:
            result = "mille"
        else:
            result = self.convert(thousand) + " mille"
        if remainder == 0:
            return result
        return result + " " + self.convert(remainder)
