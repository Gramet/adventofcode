"""Download input for a given day and year (defaults to 2022)"""
import fire
import requests

from utils import (INPUT_URL, REQUEST_HEADERS, SESSION_TOKEN,
                   input_data_is_downloaded, save_input)


def download_input(
    day: int,
    year: int = 2022,
):
    """Download file from a advent of code server and save it for future reference"""
    if not input_data_is_downloaded(year, day):
        input_url = INPUT_URL.format(year, day)
        html_data = requests.get(
            input_url,
            cookies={"session": SESSION_TOKEN},
            headers=REQUEST_HEADERS,
            timeout=5,
        )
        save_input(year, day, html_data.text)
    else:
        print(f"Input data already downloaded for year {year} day {day}")


if __name__ == "__main__":
    fire.Fire(download_input)
