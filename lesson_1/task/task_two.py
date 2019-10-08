country_dict = {
    'Ukraine': 'Kiev',
    'Russia': 'Moskow',
    'USA': 'Washington',
}

country_list = ['Ukraine', 'Poland', 'USA']

for i in country_list:
    if i in country_dict:
        print(country_dict.get(i))
