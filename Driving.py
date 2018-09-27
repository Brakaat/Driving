age = int(input('How old are you?\n'))
country = input('What country are you come from? US/TW/else\n')
# if country != ('US', 'TW', 'else'):
#     print('invalid command line')
if country == 'TW':
    if age >= 18:
        print('You can drive!')
    else:
        print('You can\'t drive!')
if country == 'US':
    if age >= 16:
        print('You can drive!')
    else:
        print('You can\'t drive!')