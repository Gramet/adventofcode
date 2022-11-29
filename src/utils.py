"""Utils for file handling"""
import os
from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

SESSION_TOKEN = os.environ["session"]
INPUT_URL = "https://adventofcode.com/{}/day/{}/input"
SUBMIT_URL = "https://adventofcode.com/{}/day/{}/answer"
DAY_TEMPLATE = Path(__file__).parent.parent / "year_template" / "template"


def get_year_path(year: int):
    """Get path to a specific year

    Args:
        year (int): Year

    Returns:
        Path: Path to the folder of that year
    """
    return Path(__file__).parent.parent / str(year)


def get_day_path(year: int, day: int):
    """Get path to a specific day and year

    Args:
        year (int): Year
        day (int): Day

    Returns:
        Path: Path to the folder of that day and year
    """
    return get_year_path(year) / f"day{day}"


def _get_input_path(year: int, day: int):
    """Get path to a specific input file (day and year)

    Args:
        year (int): Year
        day (int): Day

    Returns:
        Path: Path to the input file of that day and year
    """
    return get_day_path(year, day) / "input"


def _get_answer_path(year: int, day: int, part: int):
    """Get path to a specific answer file (day, year and part)

    Args:
        year (int): Year
        day (int): Day
        part (int): Part

    Returns:
        Path: Path to the answer file of that part, day and year
    """
    return get_day_path(year, day) / f"part{part}"


def input_data_is_downloaded(year: int, day: int):
    """Check if input data is already downloaded

    Args:
        year (int): Year
        day (int): Day

    Returns:
        bool: Whether the input file already exists
    """
    return _get_input_path(year, day).is_file()


def save_input(year: int, day: int, input_data):
    """Save data in input file

    Args:
        year (int): Year
        day (int): Day
        input_data (str): Input data from AoC
    """
    with open(_get_input_path(year, day), "w+", encoding="utf-8") as opened_file:
        opened_file.write(input_data)


def get_solution(year: int, day: int, part: int) -> str:
    """Get solution from solution file

    Args:
        year (int): Year
        day (int): Day
        part (int): Part
    """
    with open(_get_answer_path(year, day, part), "r", encoding="utf-8") as opened_file:
        data = opened_file.read()
        return data
