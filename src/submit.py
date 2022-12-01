"""Submit answers
Take as input the day, part and year (defaults to 2022)
"""
import fire
import requests

from utils import REQUEST_HEADERS, SESSION_TOKEN, SUBMIT_URL, get_solution


def submit_solution(day: int, part: int, year: int = 2022) -> str:
    """Submit solution output to a advent of code server"""
    submit_url = SUBMIT_URL.format(year, day)
    output = get_solution(year, day, part)
    data = {"level": part, "answer": output}
    response = requests.post(
        submit_url,
        data,
        cookies={"session": SESSION_TOKEN},
        headers=REQUEST_HEADERS,
        timeout=5,
    )
    if response.status_code != 200:
        message = "Error submitting solution online. Returned non 200 status code"
    else:
        text_data = response.text
        if "too high" in text_data:
            message = "Your answer is too high"
        elif "too low" in text_data:
            message = "Your answer is too low"
        elif "That's not" in text_data:
            message = "That's not the right answer"
        elif "You don't seem" in text_data:
            message = "You don't seem to be solving right level"
        elif "You gave an answer" in text_data:
            message = "You have to wait for 1 min before submitting next solution"
        elif "That's the right answer" in text_data:
            message = "Congratulation, you have solved question successfully"
        else:
            message = "Got unknown message. Please retry if answered is not submitted: {text_data}"
    print(message)


if __name__ == "__main__":
    fire.Fire(submit_solution)
