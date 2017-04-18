import math

checked = {}
atans = {}

def visiblePoints(points):
    max_found = 0
    min_angle = 0
    s = len(points)
    for i in range(0,s):
        mx = float(points[i][0])
        my = float(points[i][1])

        min_angle = getatan2(my,mx)
        
        if min_angle in checked:
            continue
        
        found = 0        
        max_angle = min_angle+0.7853981634
        
        for j in range(0,s):
            x = float(points[j][0])
            y = float(points[j][1])
            
            if (x * -1 == mx) and (y * -1 == my):
                continue
            
            angle = getatan2(y,x)
            
            if angle >= min_angle and angle < max_angle:
                found = found + 1
                
        checked[min_angle] = found
        max_found = max(found,max_found)
    return max_found

def getatan2(x,y):
    key = str(x)+str(y)
    if key in atans:
        return atans[key]
    val = math.atan2(y,x)
    atans[key] = val
    return val
