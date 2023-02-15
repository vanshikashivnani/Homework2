try:
    gross = int(input('What is your gross salary?'))
except ValueError:
    print('Sorry, invalid number.')
if gross < 1000:
    print(gross*0.1, '€ will be deducted from your gross salary due to income tax')
    print('So, your net salary is', gross - gross*0.1, '€')

if gross < 2000 and gross > 1000:
    print(gross*0.12, '€ will be deducted from your gross salary due to income tax')
    print('So, your net salary is', gross - gross*0.12, '€')

elif gross < 4000 and gross > 2000:
    print(gross*0.14, '€ will be deducted from your gross salary due to income tax')
    print('So, your net salary is', gross - gross*0.14, '€')

elif gross > 4000:
    print(gross * 0.18, '€ will be deducted from your gross salary due to income tax')
    print('So, your net salary is', gross - gross*0.18, '€')

try:
    child = int(input('How many children do you have?'))
except ValueError:
    print('Sorry, invalid data.')
if gross < 2000 and gross > 1000:
    print('Your tax cut is of', gross*0.01*child, '€')
    print('So, you are actually getting', (gross-gross*0.12)+(gross*0.01*child), '€')

if gross < 1000:
    print('Your tax cut is of', gross*0.01 * child, '€')
    print('So, you are actually getting', (gross - gross * 0.1) + (gross * 0.01 * child), '€')

if gross > 2000 and gross < 4000:
    print('Your tax cut is of', gross*0.005 * child, '€')
    print('So, you are actually getting', (gross - gross * 0.14) + (gross * 0.005 * child), '€')

if gross > 4000:
    print('Your tax cut is of', gross * 0.005 * child, '€')
    print('So, you are actually getting', (gross - gross * 0.18) + (gross * 0.005 * child), '€')


