def sorted_map(map):
    map=sorted(list(map.items()),key=lambda x:x[1],reverse=True)
    return map