# My method
def friend(x):
    return [name for name in x if len(name) == 4]

# Method 1
def friend(x):
    return list(filter(lambda name: len(name)==4, x))



lst = ["Ryan", "Kieran", "Mark"]
friend(lst)

