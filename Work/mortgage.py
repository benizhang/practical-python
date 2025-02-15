# mortgage.py
#
# Exercise 1.7

principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

payment_month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    total_payment = 0
    payment_month += 1
    if payment_month >= extra_payment_start_month and payment_month <= extra_payment_end_month:
        total_payment = payment + extra_payment
    else:
        total_payment = payment
    principal = principal * (1+rate/12) - total_payment

    if principal < 0:
        total_payment = abs(principal)
        principal = 0

    total_paid = total_paid + total_payment
    print(payment_month, round(total_paid, 2), round(principal, 2))


print('Total paid', round(total_paid, 2))
print('Months', payment_month)


