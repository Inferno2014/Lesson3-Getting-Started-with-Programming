temperature = int(input('Enter temperature in celsius: '))
if temperature<30:
    print('It is normal, choose your outfit')
else:
    print('It is hot, so wear cotton clothes')
rain = input('Is it raining?: ')
if rain=='yes':
    print('Wear a raincoat and boots and carry an umbrella')
else:
    print('Wear cotton clothes')
outfit = input('Enter your outfit here: ')
if temperature<30 and rain=='yes':
    print('I suggest wearing a raincoat')
elif temperature<30 and rain=='no':
    print('Wear woollen clothes')
elif temperature>30 and rain=='no':
    print('Wear your selected outfit,',outfit)
shoes = input('Enter your shoes here: ')
if temperature<30 and rain=='yes':
    print('I suggest wearing boots')
elif temperature>30 and rain=='no':
    print('Wear your selected shoes,',shoes)
elif temperature<30 and rain=='no':
    print('Wear your selected shoes',shoes)
accessory = input('Do you want any accessories?: ')
if accessory=='yes':
    accessory2 = input('Enter the selected accessory here: ')
    print('You have selected',accessory2)