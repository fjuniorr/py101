"""Car Loan Calculator

Calculate monthly payments (with interest compounded monthly) given:

- loan amount
- annual percentage rate (apr)
- loan duration
"""

import locale
import re
import os
import json

locale.setlocale(locale.LC_ALL, "")
# locale.setlocale(locale.LC_ALL, "pt_BR.utf-8") # for testing
LANG, _ = locale.getlocale()

with open("lesson2/21-loan-calculator.json") as fs:
    MESSAGES = json.load(fs)

def main():
    """Ask for user parameters and display results (possibly multiple times)"""
    calculator()
    while keep_going():
        clear()
        calculator()


def calculator():
    prompt("title", add_prompt_symbol=False)
    loan_amount = get_loan_amount()
    annual_percentage_rate = get_annual_percentage_rate()
    loan_duration_in_months = get_loan_duration_in_yearmonth()
    monthly_payment = calculate_monthly_payment(
        loan_amount, annual_percentage_rate / 12, loan_duration_in_months
    )
    prompt("result", value=locale.currency(monthly_payment, grouping=True))


def keep_going():
    prompt("keep_going")
    if input().strip().lower() in ["y", "yes"]:
        return True
    return False


def clear():
    if os.name == "posix":
        _ = os.system("clear")  # mac/linux
    else:
        _ = os.system("cls")  # windows


def calculate_monthly_payment(principal, interest, duration):
    result = principal * (interest / (1 - (1 + interest) ** (-duration)))
    return result


def get_loan_amount():
    """Asks for loan amount until a valid one (ie. positive number) is entered."""
    prompt("loan_amount")
    user_input = input()
    loan_amount = parse_loan_amount(user_input)

    while not loan_amount:
        prompt("invalid_loan_amount", value=user_input)
        user_input = input()
        loan_amount = parse_loan_amount(user_input)

    return loan_amount


def parse_loan_amount(number):
    try:
        result = float(number)
        return result if result > 0 else None
    except ValueError:
        return None


def get_annual_percentage_rate():
    prompt("annual_percentage_rate")
    user_input = input()
    result = parse_annual_percentage_rate(user_input)

    while not result:
        prompt("invalid_annual_percentage_rate", value=user_input)
        user_input = input()
        result = parse_annual_percentage_rate(user_input)

    return result


def parse_annual_percentage_rate(rate):
    rate = rate.strip()

    if not rate.endswith("%"):
        return False  # avoid guessing if input of "0.5" is 0.5 or 0.005

    try:
        result = float(rate.rstrip("%")) / 100
        if result == 0:
            return False  # no-interest loans are not allowed
        return result
    except ValueError:
        return False


assert parse_annual_percentage_rate("10.5%") == 0.105
assert parse_annual_percentage_rate("10%") == 0.1
assert not parse_annual_percentage_rate("0.5")
assert parse_annual_percentage_rate("0%") is False


def get_loan_duration_in_yearmonth():
    prompt("loan_duration_in_yearmonth")
    user_input = input()
    result = parse_loan_duration_in_yearmonth(user_input)

    while not result:
        prompt("invalid_loan_duration_in_yearmonth", value=user_input)
        user_input = input()
        result = parse_loan_duration_in_yearmonth(user_input)

    return result


def parse_loan_duration_in_yearmonth(yearmonth_duration):
    """Accepts strings with the following format:

    - 2y (24 months)
    - 1.5y (18 months)
    - 1y2m (14 months)
    - 10m (10 months)
    """
    pattern = re.compile(
        r"""
    (?:
        (\d*\.?\d*) # Optional group: match integer of float
        y
    )?
    (?:
        (\d+)      # Optional group: match integer
        m
    )?
    """,
        re.VERBOSE,
    )

    match = pattern.fullmatch(yearmonth_duration.strip())

    if not match:
        return None

    years = float(match.group(1)) if match.group(1) else 0.0
    months = int(match.group(2)) if match.group(2) else 0

    return int(years * 12 + months)


assert parse_loan_duration_in_yearmonth("0.5y") == 6
assert parse_loan_duration_in_yearmonth("1y2m") == 14
assert parse_loan_duration_in_yearmonth("6m") == 6
assert parse_loan_duration_in_yearmonth("1.5y") == 18
assert not parse_loan_duration_in_yearmonth("0.5m")
assert not parse_loan_duration_in_yearmonth("am")
assert not parse_loan_duration_in_yearmonth("ym")


def prompt(message_slug, add_prompt_symbol=True, **kwargs):
    message = get_message(message_slug, LANG)
    if add_prompt_symbol:
        if kwargs:
            message = message.format(**kwargs)
        print(f">>> {message}")
    else:
        print(message)


def get_message(slug, language):
    fallback = MESSAGES["en_US"][slug]
    result = MESSAGES.get(language, {}).get(slug)
    return result or fallback


if __name__ == "__main__":
    main()
