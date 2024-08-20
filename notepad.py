"""Car Loan Calculator

Calculate monthly payments (with interest compounded montthly) given:

- loan amount
- annual percentage rate (apr)
- loan duration
"""

import locale

LANG = "pt_BR"
ENCODING = "utf-8"
locale.setlocale(locale.LC_ALL, (LANG, ENCODING))

MESSAGES = {
    "en_US": {
        "title": "=== Car Loan Calculator ===",
        "loan_amount": "Enter a loan amount:",
        "invalid_loan_amount": "{value!r} is not a valid number. Enter a valid loan amount:",
        "annual_percentage_rate": "Enter your annual percentage rate (APR):",
        "invalid_annual_percentage_rate": "{value!r} is not a valid number. Enter a valid annual percentage rate (APR):",
        "loan_duration_in_years": "Enter your loan duration (in years):",
        "invalid_loan_duration_in_years": "{value!r} is not a valid number. Enter a valid loan duration (in years):",
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
    loan_duration_in_years = get_loan_duration_in_years()
    monthly_payment = calculate_monthly_payment(
        loan_amount, annual_percentage_rate / 12, loan_duration_in_years * 12
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
    result = input()

    while not is_valid_number(result):
        prompt("invalid_annual_percentage_rate", value=result)
        result = input()

    return float(result)


def get_loan_duration_in_years():
    prompt("loan_duration_in_years")
    result = input()

    while not is_valid_number(result):
        prompt("invalid_loan_duration_in_years", value=result)
        result = input()

    return float(result)


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
