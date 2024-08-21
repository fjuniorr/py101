"""Car Loan Calculator

Calculate monthly payments (with interest compounded montthly) given:

- loan amount
- annual percentage rate (apr)
- loan duration
"""

import locale
import re

LANG = "pt_BR"
ENCODING = "utf-8"
locale.setlocale(locale.LC_ALL, (LANG, ENCODING))

MESSAGES = {
    "en_US": {
        "title": "=== Car Loan Calculator ===",
        "loan_amount": "Enter a loan amount:",
        "invalid_loan_amount": "{value!r} is not valid. Enter a valid loan amount:",
        "annual_percentage_rate": "Enter your annual percentage rate (eg. 10.5%):",
        "invalid_annual_percentage_rate": "{value!r} is not valid. Enter a valid annual percentage rate (eg. 10.5%):",
        "loan_duration_in_years": "Enter your loan duration (eg. 2y; 1.5y; 1y2m; 10m):",
        "invalid_loan_duration_in_years": "{value!r} is not valid. Enter a valid loan duration (eg. 2y; 1.5y; 1y2m; 10m):",
        "result": "Your monthly payment is ${value:n}",
    },
    "pt_BR": {
        "title": "=== Calculadora Empréstimo Carros ===",
        "result": "Sua prestação mensal é R$ {value:n}",
    },
}


def main():
    """Ask for parameters and display results"""
    prompt("title", add_prompt_symbol=False)
    loan_amount = get_loan_amount()
    annual_percentage_rate = get_annual_percentage_rate()
    loan_duration_in_months = get_loan_duration_in_yearmonth()
    monthly_payment = calculate_monthly_payment(
        loan_amount, annual_percentage_rate / 12, loan_duration_in_months
    )
    prompt("result", value=monthly_payment)


def calculate_monthly_payment(principal, interest, duration):
    result = principal * (interest / (1 - (1 + interest) ** (-duration)))
    return result


def get_loan_amount():
    prompt("loan_amount")
    result = input()

    while not is_valid_number(result):
        prompt("invalid_loan_amount", value=result)
        result = input()

    return float(result)


def get_annual_percentage_rate():
    prompt("annual_percentage_rate")
    user_input = input()
    result = is_valid_annual_percentage_rate(user_input)

    while not result:
        prompt("invalid_annual_percentage_rate", value=user_input)
        user_input = input()
        result = is_valid_annual_percentage_rate(user_input)

    return result

def is_valid_annual_percentage_rate(rate):
    rate = rate.strip()
    
    if not rate.endswith("%"):
        return False # avoid guessing if input of "0.5" is 0.5 or 0.005

    try:
        result = float(rate.rstrip("%")) / 100
        if result == 0:
            return False # no-interest loans are not allowed
        return result
    except ValueError:
        return False

assert is_valid_annual_percentage_rate("10.5%") == 0.105
assert is_valid_annual_percentage_rate("10%") == 0.1
assert not is_valid_annual_percentage_rate("0.5")
assert is_valid_annual_percentage_rate("0%") is False

def get_loan_duration_in_yearmonth():
    prompt("loan_duration_in_years")
    user_input = input()
    result = is_valid_yearmonth(user_input)

    while not result:
        prompt("invalid_loan_duration_in_years", value=user_input)
        user_input = input()
        result = is_valid_yearmonth(user_input)

    return result

def is_valid_yearmonth(yearmonth_duration):
    """Accepts strings with the following format:

    - 2y (24 months)
    - 1.5y (18 months)
    - 1y2m (14 months)
    - 10m (10 months)
    """
    pattern = re.compile(r"""
    (?:
        (\d*\.?\d*)  # Optional group 1: Match 0 or more digits followed by an optional decimal point and 0 or more digits (e.g., '1', '0.5', '2.0')
        y            # Match the character 'y' which indicates years
    )?
    (?:
        (\d+)        # Optional group 2: Match 1 or more digits (e.g., '2', '12') which indicates months
        m            # Match the character 'm' which indicates months
    )?
    """, re.VERBOSE)
    
    match = pattern.fullmatch(yearmonth_duration.strip())
    
    if not match:
        return None
    
    years = float(match.group(1)) if match.group(1) else 0.0
    months = int(match.group(2)) if match.group(2) else 0
        
    return int(years * 12 + months)

assert is_valid_yearmonth("0.5y") == 6
assert is_valid_yearmonth("1y2m") == 14
assert is_valid_yearmonth("6m") == 6
assert is_valid_yearmonth("1.5y") == 18
assert not is_valid_yearmonth("0.5m")
assert not is_valid_yearmonth("am")
assert not is_valid_yearmonth("ym")

def is_valid_number(number):
    try:
        float(number)
        return True
    except ValueError:
        return False

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
    result = MESSAGES[language].get(slug)
    return result or fallback


if __name__ == "__main__":
    main()
