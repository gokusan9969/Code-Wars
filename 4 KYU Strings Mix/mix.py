from collections import Counter

def mix(s1, s2):
    c_s1 = Counter(filter(str.islower, s1))
    c_s2 = Counter(filter(str.islower, s2))
    
    result = []
    
    c1 = set(c_s1.keys())
    c2 = set(c_s2.keys())
    
    for x in (c1 | c2):
        n1 = c_s1.get(x,0)
        n2 = c_s2.get(x,0)
        
        if n1 > 1 or n2 > 1:
            if n1 > n2:
                result.append("1:" + x * n1)
        
            elif n1 < n2:
                result.append("2:" + x * n2)
        
            else:
                result.append("=:" + x * n1)
        
    return "/".join(sorted(result, key=lambda s: (-len(s), s)))
