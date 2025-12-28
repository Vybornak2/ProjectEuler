import argparse
import json
import re
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md


def main(problem_id: int) -> None:
    task_info = extract_problem_info(problem_id)
    if "error" in task_info:
        print(f"Error extracting problem info: {task_info['error']}")
        return

    create_task(task_info)


def create_task(task_info: dict[str, str | int]) -> None:
    """Create task files in problem list directory.

    Files created:
    1. directory p_xxx_problem_name in problem_list directory
    2. desc_p_xxx_problem_name
    3. solution_p_xxx_problem_name.ipynb

    Args:
        task_info (dict[str, str | int]): Dictionary containing problem information.
    """
    problem_id = int(task_info["problem_id"])
    header = str(task_info["header"])
    description = str(task_info["description"])
    url = str(task_info["url"])

    # Sanitize name for filename
    # Remove special characters, replace spaces with underscores
    safe_name = re.sub(r"[^\w\s-]", "", header).strip().replace(" ", "_")

    folder_name = f"p_{problem_id:03d}_{safe_name}"

    # Determine project root.
    # Assuming this script is at tools/task_creator/task_creator.py
    current_file = Path(__file__)
    # Go up 3 levels: tools/task_creator/ -> tools/ -> ProjectEuler/
    project_root = current_file.parents[2]
    problem_list_dir = project_root / "problem_list"

    if not problem_list_dir.exists():
        # Fallback if structure is different or running from elsewhere
        # Try CWD
        if (Path.cwd() / "problem_list").exists():
            problem_list_dir = Path.cwd() / "problem_list"
        else:
            # Create it in project root
            problem_list_dir.mkdir(exist_ok=True)

    task_dir = problem_list_dir / folder_name
    task_dir.mkdir(parents=True, exist_ok=True)

    # Create description file
    desc_filename = f"desc_p_{problem_id:03d}_{safe_name}.md"
    desc_path = task_dir / desc_filename

    full_description = f"# {header}\n\n[Problem Link]({url})\n\n{description}"
    desc_path.write_text(full_description, encoding="utf-8")

    # Create solution notebook
    solution_filename = f"solution_p_{problem_id:03d}_{safe_name}.ipynb"
    solution_path = task_dir / solution_filename

    template_path = Path(__file__).parent / "solution.ipynb"

    if not solution_path.exists():
        if template_path.exists():
            solution_path.write_bytes(template_path.read_bytes())
        else:
            notebook_content = {
                "cells": [],
                "metadata": {},
                "nbformat": 4,
                "nbformat_minor": 4,
            }
            solution_path.write_text(
                json.dumps(notebook_content, indent=1), encoding="utf-8"
            )

    print(f"Created task files in: {task_dir}")


def extract_problem_info(problem_id: int) -> dict[str, str | int]:
    """Extract problem information from Project Euler.

    Args:
        problem_id (int): The Project Euler problem ID.

    Returns:
        dict[str, str | int]: A dictionary containing problem information.
    """
    url = f"https://projecteuler.net/problem={problem_id}"
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        return {"error": str(e)}

    soup = BeautifulSoup(response.content, "html.parser")

    # Extract Header
    header_text = ""
    content_div = soup.find("div", id="content")
    if content_div:
        h2 = content_div.find("h2")
        if h2:
            header_text = h2.get_text().strip()

    # Extract Description
    description_text = ""
    problem_content = soup.find("div", class_="problem_content")
    if not problem_content:
        problem_content = soup.find("div", id="problem_content")

    if problem_content:
        # Convert to Markdown using markdownify
        # We pass the HTML string of the element
        html_content = str(problem_content)
        description_text = md(html_content, heading_style="ATX").strip()

        # Clean up excessive newlines
        description_text = re.sub(r"\n{3,}", "\n\n", description_text)

        # Unescape underscores in math blocks (simple approach: unescape all,
        # as underscores in text are rare in PE problems and usually mean math)
        # But let's try to be slightly safer: unescape \_
        description_text = description_text.replace(r"\_", "_")

    return {
        "problem_id": problem_id,
        "url": url,
        "header": header_text,
        "description": description_text,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create Project Euler task files.")
    parser.add_argument("problem_id", type=int, help="The Project Euler problem ID")
    args = parser.parse_args()
    main(args.problem_id)

    # for i in range(1, 42):
    # main(i)
