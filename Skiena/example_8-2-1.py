MATCH = 0
INSERT = 1
DELETE = 2
MAX_TYPE = 3

def calc_distance_recursive(a, b):
    opt = [None, None, None]
    
    if(a==""): return len(b)
    if(b==""): return len(a)

    opt[MATCH]  = calc_distance_recursive(a[0:len(a)-1], b[0:len(b)-1]) + int(a[len(a)-1]!=b[len(b)-1])
    opt[INSERT] = calc_distance_recursive(a[0:len(a)-1], b[0:len(b)-2]) + 1
    opt[DELETE] = calc_distance_recursive(a[0:len(a)-2], b[0:len(b)-1]) + 1
    
    return (min(opt[MATCH], opt[INSERT], opt[DELETE]))

print(calc_distance_recursive("shotagohour", "spotagogour"))
print(calc_distance_recursive("shot", "spot"))