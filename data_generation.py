#data generation file, generates a set of data for testing. 

from random import randint

def generate_uncorrelated(num_of_points, mins, maxs, dimensions):
    data = []
    for point_num in range(num_of_points): #for each point
        point = []
        for dimension in range(dimensions): #for each dimension
            dim_point = randint(mins[dimension], maxs[dimension]) #generate a value for the dimension
            point.append(dim_point)
        data.append(point)
    return data


if __name__ == "__main__":
    data = generate_uncorrelated(100, [-10,-10,-10], [10,10,10], 3)
    print(data[0])
    print(data[1])
    print(data[2])