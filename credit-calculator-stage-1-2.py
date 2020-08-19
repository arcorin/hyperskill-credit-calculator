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
