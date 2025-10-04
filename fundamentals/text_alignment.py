"""
This module demonstrates various text alignment techniques in Python using string methods and f-string.
String methods (ljust, rjust, center) are used to align only strings, while f-strings can be used for formatting numbers as well.

P.s. formatting numbers or combining multiple styles (like decimals, signs, width), f-strings are more powerful.
"""


# Function to demonstrate text alignment with string methods
def demonstrate_text_alignment() -> None:
    # text to be aligned
    text = "Align Me"

    # Left alignment using ljust
    left_aligned = text.ljust(20, '-')
    print(f"Left Aligned : '{left_aligned}'")

    # Right alignment using rjust
    right_aligned = text.rjust(20, '-')
    print(f"Right Aligned: '{right_aligned}'")

    # Center alignment using center
    center_aligned = text.center(20, '-')
    print(f"Center Aligned: '{center_aligned}'")


def demonstrate_fstring_alignment() -> None:
    # number to be aligned
    number = 42

    # Left alignment using f-string
    left_aligned = f"{number:<20}"
    print(f"Left Aligned : '{left_aligned}'")

    # Right alignment using f-string
    right_aligned = f"{number:>20}"
    print(f"Right Aligned: '{right_aligned}'")

    # Center alignment using f-string
    center_aligned = f"{number:^20}"
    print(f"Center Aligned: '{center_aligned}'")


# Call the functions
if __name__ == "__main__":
    print("\nDemonstrating Text Alignment Using String Methods")
    demonstrate_text_alignment()
    print("\nDemonstrating Text Alignment Using f-Strings")
    demonstrate_fstring_alignment()