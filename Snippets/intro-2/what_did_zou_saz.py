def fix_yz(s):
    result = ''
    for letter in s:
    if letter == 'z':
        result += 'y'
    elif letter == 'y':
        result += 'z'
    elif letter == 'Y':
        result += 'Z'
    elif letter == 'Z':
        result += 'Y'
    else:
        result += letter
    return result