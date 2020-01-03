def dirReduc(arr):

    direc_pair = {"NORTH":"SOUTH", "SOUTH":"NORTH", "EAST":"WEST", "WEST":"EAST"}
    
    new_arr = []
    
    for x in arr:
        
        if new_arr and new_arr[-1] == direc_pair[x]:
            new_arr.pop()
      
        else:
            new_arr.append(x)
            
    return new_arr
