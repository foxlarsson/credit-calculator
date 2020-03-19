import math


def calculate_count_of_months(prin, per_month, int_rate):
    nominal_int_rate = int_rate / 12
    periods = math.ceil(math.log(per_month / (per_month - nominal_int_rate * prin), 1 + nominal_int_rate))
    num_years = int(periods // 12)
    num_months = math.ceil(periods % 12)
    if num_years and num_months:
        print(f'You need {num_years} years and {num_months} months to repay this credit!')
    elif num_years:
        print(f'You need {num_years} years to repay this credit!')
    elif num_months:
        print(f'You need {num_months} months to repay this credit!')


def calculate_annuity(prin, periods, int_rate):
    nominal = int_rate / 12
    annuity = prin * (nominal * math.pow(1 + nominal, periods) / (math.pow(1 + nominal, periods) - 1))
    print(f'Your annuity payment = {math.ceil(annuity)}!')


def calculate_principal(ann, periods, int_rate):
    nominal = int_rate / 12
    prin = ann / (nominal * math.pow(1 + nominal, periods) / (math.pow(1 + nominal, periods) - 1))
    print(f'Your credit principal = {round(prin)}!')


def main():
    action = input('What do you want to calculate?\n'      
                   'type "n" - for count of months\n'      
                   'type "a" for annuity monthly payment\n'
                   'type "p - for credit principal:\n')
    if action == 'n':
        principal = float(input('Enter credit principal:\n'))
        monthly = float(input('Enter monthly payment:\n'))
        interest = float(input('Enter credit interest:\n')) / 100
        calculate_count_of_months(principal, monthly, interest)
    elif action == 'a':
        principal = float(input('Enter credit principal:\n'))
        num_periods = float(input('Enter count of periods:\n'))
        interest = float(input('Enter credit interest:\n')) / 100
        calculate_annuity(principal, num_periods, interest)
    elif action == 'p':
        monthly = float(input('Enter monthly payment:\n'))
        num_periods = float(input('Enter count of periods:\n'))
        interest = float(input('Enter credit interest:\n')) / 100
        calculate_principal(monthly, num_periods, interest)


main()
