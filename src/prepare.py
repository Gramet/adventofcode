"""CLI to prepare folder for a given year"""

import shutil

import fire

from utils import DAY_TEMPLATE, get_day_path, get_year_path


def prepare_year(year: int):
    """Prepare folder for a year

    Args:
        year (int): Year
    """
    get_year_path(year).mkdir(exist_ok=True)

    for day in range(1, 26):
        if not get_day_path(year, day).is_dir():
            shutil.copytree(DAY_TEMPLATE, get_day_path(year, day))


if __name__ == "__main__":
    fire.Fire(prepare_year)
