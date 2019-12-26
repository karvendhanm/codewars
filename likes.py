lst1 = [] # 'no one likes this'
lst2 = ['Peter'] # 'Peter likes this'
lst3 = ['Jacob', 'Alex'] # 'Jacob and Alex like this'
lst4 = ['Max', 'John', 'Mark'] # 'Max, John and Mark like this'
lst5 = ['Alex', 'Jacob', 'Mark', 'Max'] # 'Alex, Jacob and 2 others like this'

# My method
def likes(names):
    ln = len(names)
    if ln < 2:
        return ("".join(names) if ln == 1 else "no one")+' likes this'
    else:
        return (", ".join(names[:(ln-1)])+ ' and '+names[-1] if len(names[2:]) <= 1 else ", ".join(names[:2])+ ' and '+str(len(names[2:]))+' others') + ' like this'

# Best Method - Just amazing
def likes(names):
    n = len(names)
    return {
        0:'no one likes this',
        1:'{} likes this',
        2:'{} and {} like this',
        3: '{}, {} and {} like this',
        4: '{}, {} and {others} others like this'
    }[min(n, 4)].format(*names[:3] ,others=n-2)


for i in [lst1, lst2, lst3, lst4, lst5]:
    print(likes(i))














