import math

def visiblePoints(points):
    
    # quick check
    s = len(points)
    if s == 1:
        return 1
    
    # create a list of angles from given points
    angles = [math.atan2(points[x][1],points[x][0]) for x in xrange(0,s)]     
    angles.sort()    
    size = len(angles)
    max_points_found = 0

    # iterate through points
    for i in range(0,size-1):
        
        # setup the min / max values
        min_angle = angles[i]
        max_angle = min_angle + 0.7853981634
        points_found = 1
        
        index = i + 1
        min_index = (index + max_points_found - 1) % size
        
        # check if the next index that is same length is still valid in range
        if angles[min_index] > max_angle or angles[min_index] < min_angle:
            continue
        
        # find all the points in the given range
        while min_angle <= angles[index] <= max_angle:
            index = (index + 1) % size
            points_found = points_found + 1
            if index == i:
                break
        
        # update max points if neccessary
        if points_found > max_points_found:
            max_points_found = points_found
        
        # break if points match list length
        if abs(max_points_found - s) == 0:
            return max_points_found

    # return max points
    return max_points_found
