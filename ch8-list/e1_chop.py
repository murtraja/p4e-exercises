def chop(list):
    if len(list) == 0:
        return
    del list[0]
    if len(list) == 0:
        return
    del list[len(list)-1]

def middle(list):
    if len(list) <= 2:
        return []
    return list[1:-1]

l = [1,2,3,4,5]
print(middle(l))
chop(l)
print(l)