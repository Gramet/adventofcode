from datetime import datetime
from typing import Optional

import typer
from typing_extensions import Annotated

from download import download_input
from get_stars import update_stars
from prepare import prepare_year
from submit import submit_solution

app = typer.Typer()


@app.command()
def get_stars():
    update_stars()


@app.command()
def download(
    day: Annotated[int, typer.Argument()] = datetime.now().day,
    year: Annotated[int, typer.Argument()] = datetime.now().year,
):
    download_input(day, year)


@app.command()
def submit(
    day: Annotated[int, typer.Argument()] = datetime.now().day,
    part: Annotated[int, typer.Argument()] = 1,
    year: Annotated[int, typer.Argument()] = datetime.now().year,
):
    submit_solution(day, part, year)


@app.command()
def prepare(year: Annotated[int, typer.Argument()] = datetime.now().year):
    prepare_year(year)


def main():
    app()


if __name__ == "__main__":
    main()
