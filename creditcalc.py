import argparse
import sys
import math

parser = argparse.ArgumentParser('\nCalculate your credit payments (differentiated or annuity.\n')
parser.add_argument('--type', help='Type of payment: '
                                   '"diff" for differentiated'
                                   '"annuity" for annuity'
                                   'Must be specified.')
parser.add_argument('--payment', type=float, help='Monthly payment, only for annuity type.')
parser.add_argument('--principal', type=float, help='Your credit principal')
parser.add_argument('--periods', type=int, help='The number of months to repay your credit')
parser.add_argument('--interest', type=float, help='Your credit interest'
                                                   'Do not use a percent sign.'
                                                   'Must to be specified.')
args = parser.parse_args()
param_error = 'Incorrect parameters'
all_parameters = [args.payment, args.principal, args.periods, args.interest]
type_values = ['annuity', 'diff']


def exit_on_param_error():
    print(param_error)
    sys.exit()


def check_args():
    if len(sys.argv) < 5:
        exit_on_param_error()
    elif args.type not in type_values:
        exit_on_param_error()
    elif args.type is None:
        exit_on_param_error()
    elif args.type == 'diff' and args.payment is not None:
        exit_on_param_error()
    elif args.interest is None:
        exit_on_param_error()
    else:
        for param in all_parameters:
            if param is not None:
                if param < 0:
                    exit_on_param_error()


def calculate_diff_payment(interest, periods, principal):
    total = 0
    interest = interest / 12 / 100
    for period in range(1, periods + 1):
        period_payment = math.ceil(principal / periods + interest * (principal - (principal * (period - 1)) / periods))
        total += period_payment
        print(f'Month {period}: paid out {period_payment}')
    overpayment = math.ceil(total - principal)
    print(f'\nOverpayment = {overpayment}')


def print_overpayment(payment, periods, principal):
    overpayment = math.ceil(payment * periods - principal)
    print(f'Overpayment = {overpayment}')


def calculate_annuity_payment(principal, periods, interest):
    payment = math.ceil(
        principal * (interest * math.pow(1 + interest, periods) / (math.pow(1 + interest, periods) - 1)))
    print(f'Your annuity payment = {payment}!')
    print_overpayment(payment, periods, principal)


def calculate_annuity_periods(principal, payment, interest):
    periods = math.ceil(math.log(payment / (payment - interest * principal), 1 + interest))
    num_years = math.ceil(periods // 12)
    num_months = math.ceil(periods % 12)
    if num_years and num_months:
        print(f'You need {num_years} years and {num_months} months to repay this credit!')
    elif num_years:
        print(f'You need {num_years} years to repay this credit!')
    elif num_months:
        print(f'You need {num_months} months to repay this credit!')
    print_overpayment(payment, periods, principal)


def calculate_annuity_principal(payment, periods, interest):
    principal = payment / (interest * math.pow(1 + interest, periods) / (math.pow(1 + interest, periods) - 1))
    print_overpayment(payment, periods, principal)


def main():
    check_args()
    if args.type == 'diff':
        calculate_diff_payment(args.interest, args.periods, args.principal)
    elif args.type == 'annuity':
        args.interest = args.interest / 12 / 100
        if args.payment is None:
            calculate_annuity_payment(args.principal, args.periods, args.interest)
        elif args.periods is None:
            calculate_annuity_periods(args.principal, args.payment, args.interest)
        elif args.principal is None:
            calculate_annuity_principal(args.payment, args.periods, args.interest)


main()
