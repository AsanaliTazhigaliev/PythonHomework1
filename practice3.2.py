months = {12: 'December', 1: 'January', 2: 'February',
          3: 'March', 4: 'April', 5: 'May',
          6: 'June', 7: 'July', 8: 'August',
          9: 'September', 10: 'October', 11: 'November'
          }


def season_events(number_of_month):
    if not isinstance(number_of_month, int) and 1 <= number_of_month <= 12:
        print('You need to enter a month number')
        return
    if number_of_month in range(3, 6):
        print(f'You were born in {months[number_of_month]}. Birds sang beautiful songs')
    elif number_of_month in range(6, 9):
        print(f'You were born in {months[number_of_month]}. The sun shone brighter than ever')
    elif number_of_month in range(9, 12):
        print(f'You were born in {months[number_of_month]}. The harvest was incredible')
    else:
        print(f'You were born {months[number_of_month]}. White snow fell outside the window')
season_events(1)
