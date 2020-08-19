import math

# Stage 1
# https://hyperskill.org/projects/90/stages/500/implement
"""
credit_principal = 'Credit principal: 1000'
final_output = 'The credit has been repaid!'
first_month = 'Month 1: paid out 250'
second_month = 'Month 2: paid out 250'
third_month = 'Month 3: paid out 500'

# write your code here
print(credit_principal)
print(first_month)
print(second_month)
print(third_month)
print(final_output)
"""


# Stage 2
# https://hyperskill.org/projects/90/stages/501/implement
'''
def calculate_months_number(principal, payment):
    months = round(principal / payment)

    suffix = "s"
    if months == 1:
        suffix = ""

    print(str(f"It takes {months} month{suffix} to repay the credit"))


def calculate_monthly_payment(principal, months):
    different_payment = int(bool(principal % months))
    payment = principal // months + 1 * different_payment
    last_payment = principal - (months - 1) * payment

    print(str(f"Your monthly payment = {payment}" + different_payment \
              * f" with last monthly payment = {last_payment}."))


def main():
    credit_principal = int(input("Enter the credit principal:\n"))

    choice = input("""What do you want to calculate?
type "m" for the number of months,
type "p" for the monthly payment:\n""")

    if choice == "m":
        monthly_payment = int(input("Enter the monthly payment:\n"))
        calculate_months_number(credit_principal, monthly_payment)

    elif choice == "p":
        months_count = int(input("Enter the count of months:\n"))
        calculate_monthly_payment(credit_principal, months_count)


main()
'''


# Stage 3
# https://hyperskill.org/projects/90/stages/502/implement

def calculate_months_number(principal, payment, interest):

    interest = interest / 100 / 12
    period = math.log(payment / (payment - interest * principal), (interest + 1))
    years = int(math.ceil(period) // 12)
    months = int(math.ceil(period) - years * 12)

    years_bool = int(bool(years))
    months_bool = int(bool(months))

    suffix_y = "s"
    if years == 1:
        suffix_y = ""

    suffix_m = "s"
    if months == 1:
        suffix_m = ""

    print("You need " + years_bool * f"{years} year{suffix_y}"
          + int(years_bool and months_bool) * " and "
          + months_bool * f"{months} month{suffix_m}" + " to repay the credit!")


def calculate_annuity_payment(principal, months, interest):
    interest = interest / 100 / 12
    payment = principal * interest * math.pow(1 + interest, months)\
        / (math.pow(1 + interest, months) - 1)
    payment = math.ceil(payment)

    print(f"Your annuity payment = {payment}!")


def calculate_credit_principal(payment, months, interest):
    interest = interest / 100 / 12
    principal = payment * (math.pow(1 + interest, months) - 1)\
        / (interest * math.pow(1 + interest, months))
    principal = int(principal)

    print(f"Your credit principal = {principal}!")


def main():

    choice = input("""What do you want to calculate?
type "n" for the count of months,
type "a" for the annuity monthly payment,
type "p" for the credit principal:\n""")

    if choice == "n":
        credit_principal = int(input("Enter the credit principal:\n"))
        monthly_payment = int(input("Enter the monthly payment:\n"))
        credit_interest = float(input("Enter the credit interest:\n"))

        calculate_months_number(credit_principal, monthly_payment, credit_interest)

    elif choice == "a":
        credit_principal = int(input("Enter the credit principal:\n"))
        months_count = int(input("Enter the number of periods:\n"))
        credit_interest = float(input("Enter the credit interest:\n"))

        calculate_annuity_payment(credit_principal, months_count, credit_interest)

    elif choice == "p":
        monthly_payment = float(input("Enter the annuity payment:\n"))
        months_count = int(input("Enter the count of periods:\n"))
        credit_interest = float(input("Enter the credit interest:\n"))

        calculate_credit_principal(monthly_payment, months_count, credit_interest)


main()
