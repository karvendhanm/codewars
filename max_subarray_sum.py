# my solution
# def maxSequence(arr):
#     lst = [0]
#     for idx1 in range(len(arr)):
#         for idx2 in range(len(arr)):
#             lst.append(sum(arr[idx1:idx2+1]))
#     return max(lst)

# Best solution
def maxSequence(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max

# function call
# assert max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6, 'function did not work'
maxSequence([1, 2, 3])


