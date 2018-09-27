age = int(input('How old are you?\n'))
country = input('What country are you come from? US/TW/else\n')
# if country != ('US', 'TW', 'else'):
#     print('invalid command line')
if country == 'TW':
    if age >= 18:
        print('You can drive!')
    else:
        print('You can\'t drive!')
elif country == 'US':
    if age >= 16:
        print('You can drive!')
    else:
        print('You can\'t drive!')
else country != 'TW' and country != 'US':
	print('Sorry, this version only accept TW and US')