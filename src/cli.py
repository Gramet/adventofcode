from datetime import datetime

import typer

from download import download_input
from get_stars import update_stars
from prepare import prepare_year
from submit import submit_solution

app = typer.Typer()


@app.command()
def get_stars():
    update_stars()


@app.command()
def download(day: int = datetime.now().day, year: int = datetime.now().year):
    download_input(day, year)


@app.command()
def submit(
    day: int = datetime.now().day, part: int = 1, year: int = datetime.now().year
):
    submit_solution(day, part, year)


@app.command()
def prepare(year: int = datetime.now().year):
    prepare_year(year)


def main():
    app()


if __name__ == "__main__":
    main()
