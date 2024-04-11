def swapPositions(lst, pos1, pos2):
    get = lst[pos1], lst[pos2]
    lst[pos2], lst[pos1] = get
    
    return lst

lst = [23, 65, 19, 90]
pos1, pos2 = 1, 3
print(swapPositions(lst, pos1-1, pos2-1))
