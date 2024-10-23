"""
Script to create a series of folders in a specified directory
"""

from pathlib import Path
import argparse as ap

FILE_DIR = Path(__file__).parent
DESC_FILE = FILE_DIR / "description.md"
SOLUTION_FILE = FILE_DIR / "solution.ipynb"


def main(i_start: int, i_end: int, path: Path) -> None:
    """
    Create a series of folders in a specified directory

    :param i_start: start index for folder creation
    :param i_end: end index for folder creation
    :param path: path to create folders in
    :raises ValueError: if start or end values are negative
    :raises ValueError: if start or end values are greater than 1000
    :raises ValueError: if start value is greater than end value
    """

    if any(i < 0 for i in [i_start, i_end]):
        raise ValueError("Start and end values must be positive integers")
    elif any(i > 1000 for i in [i_start, i_end]):
        raise ValueError("Start and end values must be less than 1000")
    elif i_start > i_end:
        raise ValueError("Start value must be less than or equal to end value")

    if not path:
        path = Path.cwd()

    for i in range(i_start, i_end + 1):
        directory_number = "0" * (3 - len(str(i))) + str(i)
        directory = path / f"p_{directory_number}"

        directory.mkdir(exist_ok=True)

        if not (solution_file := directory / SOLUTION_FILE.name).exists():
            solution_file.write_text(SOLUTION_FILE.read_text())

        if not (desc_file := directory / DESC_FILE.name).exists():
            desc_content = DESC_FILE.read_text().replace("ID", str(i))
            desc_file.write_text(desc_content)


if __name__ == "__main__":
    parser = ap.ArgumentParser()
    parser.add_argument("i_start", type=int, help="Start value for folder creation")
    parser.add_argument("i_end", type=int, help="End value for folder creation")
    parser.add_argument("--path", type=Path, help="Path to create folders in")

    args = parser.parse_args()
    main(args.i_start, args.i_end, args.path)
