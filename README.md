# adventofcode
My solution for Advent of Code problems

# Completion
<!-- begin-year-badge -->
[![](https://img.shields.io/badge/2015-0%20stars-ef0f14)](./2015)
[![](https://img.shields.io/badge/2016-0%20stars-ef0f14)](./2016)
[![](https://img.shields.io/badge/2017-0%20stars-ef0f14)](./2017)
[![](https://img.shields.io/badge/2018-26%20stars-5c6e1f)](./2018)
[![](https://img.shields.io/badge/2019-50%20stars-239323)](./2019)
[![](https://img.shields.io/badge/2020-50%20stars-239323)](./2020)
[![](https://img.shields.io/badge/2021-50%20stars-239323)](./2021)
[![](https://img.shields.io/badge/2022-50%20stars-239323)](./2022)
[![](https://img.shields.io/badge/2023-50%20stars-239323)](./2023)
[![](https://img.shields.io/badge/2024-46%20stars-2b8e22)](./2024)
<!-- end-year-badge -->

# Install

1. Get your AoC session cookie and put it in a `.env` (session=XXXXX)
2. Also set your email in `.env` to fill request headers (email=XXXXXX)
3. Install requirements using `pipenv install`

## Helpers
The package will install a typer-based cli named `aoc`. You can use it as follow:
- `aoc prepare 2022`: Will create the directories for each day of year 2022 using the template in `year_template`.
- `aoc download 1 2022`: Will download the input for problem 1 of year 2022 (NB: You need to run `prepare_year` first).
- `aoc run 1 2022`: Will run the `solution.py` file for problem 1 of year 2022.
- `aoc submit 3 1 2022`: Will submit solution for part 1 of day 3 of year 2022.
- `aoc get-stars` to update the README badges.

By default, `day` and `year` values are the current day and year. Run `aoc --help` for more details

## Workflow
- When data become available, run `aoc download`.
- Implement your solution in the `solve_part_1` and `solve_part_2` functions.
- Use `aoc submit` to submit any part once you are satisfied with it. You'll get any error message from AoC in the terminal.

