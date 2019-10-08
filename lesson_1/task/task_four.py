def get_final_deposit_amount():
    final_deposit_amount = ((deposit_amount * (percent / 100) * (number_of_years * 365)) / 365) + deposit_amount
    return final_deposit_amount


deposit_amount = float(input('Enter deposit amount:\n'))
number_of_years = float(input('Enter number of years:\n'))
percent = float(input('Enter percent:\n'))

print(get_final_deposit_amount())
