import string
def check_pass(pswd):
    err = {
        'length': 'Password length is not 8 characters',
        'upper': 'Missing capital letters',
        'lower': 'No lowercase letters in password',
        'digits': 'No numbers in the password',
        'spec': 'Missing special characters in password',
        'bad_symbols': 'Password contains unintended characters'
    }
    if len(pswd) == 8:
        err.pop('length')
    pswd_reduced = [symbol for symbol in pswd]
    for symbol in pswd:
        if symbol in string.ascii_uppercase:
            pswd_reduced.remove(symbol)
            err.pop('upper', None)
        elif symbol in string.ascii_lowercase:
            pswd_reduced.remove(symbol)
            err.pop('lower', None)
        elif symbol in string.digits:
            pswd_reduced.remove(symbol)
            err.pop('digits', None)
        elif symbol in '*-#':
            pswd_reduced.remove(symbol)
            err.pop('spec', None)
    if len(pswd_reduced) == 0:
        err.pop('bad_symbols')
    if len(err) == 0:
        print('Password is perfect')
    else:
        print(*err.values(), sep='; ')
check_pass('Write your password HERE')