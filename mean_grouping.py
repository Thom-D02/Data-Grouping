#data grouping

#splits the group equally 
def split(data, group_number):
    new_data = []
    count = 0 #counts up to keep track of the group the next point goes into
    for i in range(group_number):
        new_data.append([]) 
    for point in data:
        new_data[count].append(point)
        count += 1
        if count >= group_number:
            count = 0
    return new_data

#finds the averages of all current groups
def find_averages(data, dimension): 
    averages = []
    for group in data:
        group_average = []
        group_total = []
        for i in range(dimension):
            group_average.append(0)
            group_total.append(0)
        group_size = 0
        for point in group: #adding the point to the total
            for dim in range(len(point)):
                group_total[dim] += point[dim]
            group_size += 1
        for i in range(dimension):
            group_average[i] = group_total[i]/group_size
        averages.append(group_average)
    return averages

def find_distance(point0, point1): #finds the distance between two points. 
    if len(point0) == len(point1): 
        total = 0
        for i in range(len(point0)): #finding squared difference
            total += (point0[i] - point1[i])**2
        total = total**0.5 #square rooting the squared difference 
        return total
    return -1 #if invalid returns negative number 

def find_closest_average(point, averages):
    min_distance = find_distance(point, averages[0])
    min_group = 0
    for index in range(len(averages[1:])): #linear search through averages to find the closest
        distance = find_distance(point, averages[index + 1]) #index must be increased so it points to the right item
        if distance < min_distance and distance > 0:
            min_distance = distance
            min_group = index+1
    return min_group

def reassign(data, averages):
    newdata = [] #copying the data across 
    for group in data:
        newdata.append(group.copy())
    for group_index in range(len(data)):  #for each 
        for point_index in range(len(data[group_index])-1,-1,-1):
            closest = find_closest_average(data[group_index][point_index], averages) #finding closest average
            newdata[closest].append(data[group_index][point_index])
            newdata[group_index].pop(point_index)
    return newdata

def remove_groups(data):
    newdata = [] #copying the data across 
    for group in data:
        if len(group) > 0:
            newdata.append(group.copy())
    return newdata
