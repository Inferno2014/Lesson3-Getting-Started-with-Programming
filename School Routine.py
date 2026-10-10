day = input('What day is it(Monday - Sunday): ').strip().capitalize()
if day =='Monday':
    print('School just started. Get up and go to school')
elif day=='Friday':
    print('Last day of school week. Return all library books back')
elif day=='Tuesday' or day=='Wednesday' or day=='Thursday':
    print('Get through these days and you are home-free')
elif day=='Sunday' or day=='Saturday':
    print('It is the weekend. Go play outside and have fun')
weather = input('What is the climate(Sunny / Rainy / Cloudy): ').strip().lower()
if weather=='sunny':
    print('It is sunny outside, so be hydrated and cool')
elif weather=='rainy':
    print('It is raining, so wear a raincoat and a pair of boots, carry an umbrella')
elif weather=='cloudy':
    print('It is cloudy outside, carry an umbrella as it might rain')
homework = input('Did you finish your homework?(Yes / No): ').strip().lower()
if homework=='no':
    print('What are you waiting for, go complete it')
elif homework=='yes':
    print('Now, you can go have fun')