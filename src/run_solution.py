"""Run solution.py for a particular day
Take as input the day, part and year (defaults to 2022)
"""

from subprocess import call

import fire


def run_solution(day: int, year: int) -> None:
    """Run solution.py for given day"""
    call(["python", f"{year}/day{day}/solution.py"])


if __name__ == "__main__":
    fire.Fire(run_solution)
