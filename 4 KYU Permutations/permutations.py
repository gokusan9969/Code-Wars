def permutations(str):
    
    str_len = len(str)
    res = set([str])
    
    if str_len == 1:
        
        return str
    
    elif str_len == 2:
        
        res.add(str[1] + str[0])
    
    else:
        for a, b in enumerate(str):
            for c in permutations(str[:a] + str[a + 1:]):
                res.add(b + c)
                
    return list(res)
