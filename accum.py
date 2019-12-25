# My method
def accum(s):
    lst = []
    for idx, val in enumerate(s):
        for cnt in range(idx + 1):
            lst.append(val.upper() if cnt == 0 else val.lower())
        lst.append('-')
    return "".join(lst[:-1])

# Method 1
def accum(s):
    return "-".join(c.upper()+c.lower()*i for i, c in enumerate(s))

# Lesson: think by setting aside what is common.

accum("NyffsGeyylB")











