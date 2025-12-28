import os
import pathlib

from IPython.display import Markdown, display


def _get_desc_file_path() -> str:
    """Get the path to the markdown description file in the current directory.

    Raises:
        FileNotFoundError: If no unique description markdown file is found.

    Returns:
        str: Path to the markdown description file.
    """
    parent_dir = pathlib.Path(os.path.abspath(""))
    desc_files = list(parent_dir.glob("desc*.md"))
    if len(desc_files) != 1:
        raise FileNotFoundError(
            "Could not find a unique description markdown file in the current directory."
        )
    else:
        return str(desc_files[0])


def _display_task_description(desc_file_path: str) -> None:
    """Display the task description from a markdown file.

    Args:
        desc_file_path (str): Path to the markdown description file.
    """
    if not os.path.isfile(desc_file_path):
        print(f"Description file '{desc_file_path}' does not exist.")
        return

    with open(desc_file_path, "r") as file:
        md_content = file.read()

    display(Markdown(md_content))  # type: ignore


def display_description() -> None:
    """Display the task description from the markdown file in the current directory."""
    desc_file_path = _get_desc_file_path()
    _display_task_description(desc_file_path)


if __name__ == "__main__":
    # Example usage
    example_desc_file = "desc_p_001_multiples_of_3_and_5.md"
    _display_task_description(example_desc_file)
