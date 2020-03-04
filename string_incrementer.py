def increment_string(strng):
    if strng == "": return '1'
    if ord(list(strng)[-1]) not in range(48, 58): return strng + str(1)
    return strng

strng = "foobar001"
lst=[]
for char in strng[::-1]:
    if ord(char) in range(48, 58):
        lst.append(char)
    else:
        break


dir(str)
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha',
'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip',
'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase',
'title', 'translate', 'upper', 'zfill'
