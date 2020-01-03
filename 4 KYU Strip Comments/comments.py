from re import escape, sub

def solution(string, markers):

    if not markers:
        
        return string
    
    else:
        
        return sub(r'( *[{}].*)'.format(escape(''.join(markers))), '', string)
