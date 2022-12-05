from bs4 import BeautifulSoup
import requests
from math import sqrt
from utils import SESSION_TOKEN, REQUEST_HEADERS

MD_BADGE_URL = "https://img.shields.io/badge/{year}-{stars}%20stars-{color}"
DELIM_BEGIN = "<!-- begin-year-badge -->"
DELIM_END = "<!-- end-year-badge -->"


def rgb2hex(r, g, b):
    def f(x):
        return max(0, min(255, round(x * 255)))

    return f"{f(r):02x}{f(g):02x}{f(b):02x}"


def hex2rgb(x):
    return (int(x[:2], 16) / 255, int(x[2:4], 16) / 255, int(x[4:], 16) / 255)


def interpolate(c0, c1, t):
    x0 = hex2rgb(c0)
    x1 = hex2rgb(c1)
    return rgb2hex(*[(1 - t) * x0[i] + t * x1[i] for i in range(3)])


def get_stars():
    html_data = requests.get(
        "https://adventofcode.com/events",
        cookies={"session": SESSION_TOKEN},
        timeout=5,
        headers=REQUEST_HEADERS,
    )
    parsed_html = BeautifulSoup(html_data.text, features="html.parser")
    events = parsed_html.body.find_all("div", attrs={"class": "eventlist-event"})

    years = []
    stars = []
    for event in events:
        year = event.a.text[1:-1]
        star = 0
        if event.span is not None:
            star = int(event.span.text[:-1])
        years.append(year)
        stars.append(star)
    return years[::-1], stars[::-1]


def get_text(years, stars):
    out_text = []
    for year, star in zip(years, stars):
        # sqrt(x) > x, for x in [0, 1], so we get to green faster
        trajectory = sqrt(star / 50)
        color = interpolate("ef0f14", "239323", trajectory)

        badge = f"![]({MD_BADGE_URL.format(year=year, stars=star, color=color)})"
        badge = f"[{badge}](./{year})"

        out_text.append(badge)
    return out_text


def update_readme(text):
    with open("README.md", "rt") as fp:
        lines = [x.strip() for x in fp]

    for i, line in enumerate(lines):
        if line == DELIM_BEGIN:
            start = i
        elif line == DELIM_END:
            end = i

    out = lines[: start + 1] + text + lines[end:]

    with open("README.md", "wt") as fp:
        for line in out:
            fp.write(f"{line}\n")

    print("README updated!")


if __name__ == "__main__":
    years, stars = get_stars()
    out_text = get_text(years, stars)
    update_readme(out_text)
