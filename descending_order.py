# Method One

def descending_order(num):
    # Bust a move right here
    if isinstance(num, int) and num >=0:
        return int("".join(sorted(str(num), reverse=True)))
    else:
        return ValueError('Non-negative integer expected')

# Method Two
def descending_order(num):
    s = str(num)
    s = sorted(s)
    s = reversed(s)
    s = "".join(s)
    return int(s)


# Method three
def descending_order(num):
    return int("".join(sorted(str(num)))[::-1])

# Method four
descending_order = lambda num: int("".join(sorted(str(num), reverse=True)))

# Calling the function
descending_order(534589735735897)


