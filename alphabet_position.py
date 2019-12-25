# My method
def alphabet_position(text):
    lst = []
    alphabet_lookup = 'abcdefghijklmnopqrstuvwxyz'
    for letter in text.lower():
        try:
            lst.append(alphabet_lookup.index(letter)+1)
        except:
            continue
    return " ".join([str(idx) for idx in lst])

# Method two
def alphabet_position(text):
    return " ".join(str(ord(c)-96) for c in text.lower() if c.isalpha())

alphabet_position("The sunset sets at twelve o' clock.")
