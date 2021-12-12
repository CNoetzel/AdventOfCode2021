from typing import List

class Point:
    def __init__(self, value: int, row: int, column:int):
        self.value = value
        self.row = row
        self.column = column
    
    def __eq__(self, other):
        return self.row == other.row and self.column == other.column

    def __repr__(self):
        return f'{self.row}/{self.column} value: {self.value}'

# function to prepare data will return a multidimensional array (part 1 and part 2)
def prepare_data(lines: list) -> List[List[int]]:
    heightmap = []
    for line in lines:
        row = []
        values = list(str(line).strip())
        for value in values:
            row.append(int(value))
        heightmap.append(row)
    return heightmap

# function to return the lowest points of a heigth map (part 1 and part 2)
def get_lowest_points(heightmap: list) -> List[Point]:
    lowest_points = []
    for i in range(len(heightmap)):
        row = heightmap[i]
        for j in range(len(row)):
            value = row[j]
            if value == 9: continue
            row_modificators = []
            column_modificators = []
            if i == 0:
                row_modificators.append(1)
                if j == 0: column_modificators.append(1) # top left corner
                elif j == len(row)-1: column_modificators.append(-1) # top right corner
                else: column_modificators.extend([1,-1]) # top row
            elif i == len(heightmap)-1: 
                row_modificators.append(-1)
                if j == 0: column_modificators.append(1) # bottom left corner
                elif j == len(row)-1: column_modificators.append(-1) # bottom right corner
                else: column_modificators.extend([1,-1]) # bottom row
            else:
                row_modificators.extend([1,-1])
                if j == 0: column_modificators.append(1) # left column
                elif j == len(row)-1: column_modificators.append(-1) # right column
                else: column_modificators.extend([1,-1])
            
            # retrieve values based on modifiers and compare to value from current point
            add = True
            for row_modificator in row_modificators: 
                if value > heightmap[i+row_modificator][j]: 
                    add = False # smaller value have been found
                    break
            if add: # do not compare column if smaller value have already been found
                for column_modificator in column_modificators:
                    if value > row[j+column_modificator]:
                        add = False # smaller value have been found
                        break

            # add value if lowest point
            if add: lowest_points.append(Point(value,i,j))
    return lowest_points

# function to calculate the risk level based on a given heigth map (part 1)
def get_risk_level(heightmap: list) -> int:
    lowest_points = get_lowest_points(heightmap)
    sum = 0
    for point in lowest_points:
        sum += point.value+1
    return sum

# function to calculate the basin size based by a given start point (part 2)
def calculate_basin_size(start: Point, heightmap: list, visited_points: List[Point]):
    if start.value == 9: return 0
    visited_points.append(start)
    count = 1
    row_modificators = []
    column_modificators = []
    if start.row == 0:
        row_modificators.append(1)
        if start.column == 0: column_modificators.append(1) # top left corner
        elif start.column == len(heightmap[0])-1: column_modificators.append(-1) # top right corner
        else: column_modificators.extend([1,-1]) # top row
    elif start.row == len(heightmap)-1: 
        row_modificators.append(-1)
        if start.column == 0: column_modificators.append(1) # bottom left corner
        elif start.column == len(heightmap[0])-1: column_modificators.append(-1) # bottom right corner
        else: column_modificators.extend([1,-1]) # bottom row
    else:
        row_modificators.extend([1,-1])
        if start.column == 0: column_modificators.append(1) # left column
        elif start.column == len(heightmap[0])-1: column_modificators.append(-1) # right column
        else: column_modificators.extend([1,-1])

    for row_modificator in row_modificators:
        new_value = heightmap[start.row+row_modificator][start.column]
        new_point = Point(new_value, start.row+row_modificator, start.column)
        if new_point not in visited_points:
            visited_points.append(new_point)
            count += calculate_basin_size(new_point, heightmap, visited_points)
    
    for column_modificator in column_modificators:
        new_value = heightmap[start.row][start.column+column_modificator]
        new_point = Point(new_value, start.row, start.column+column_modificator)
        if new_point not in visited_points:
            visited_points.append(new_point)
            count += calculate_basin_size(new_point, heightmap, visited_points)
    
    return count

# function to return the basin sizes based on the calculated low points (part 2)
def get_basin_sizes(lowest_points: List[Point], heightmap: list) ->  List[int]:
    basin_sizes = []
    for point in lowest_points: basin_sizes.append(calculate_basin_size(point, heightmap, []))
    return basin_sizes

# function to return the multiplied basin size values (part 2)
def get_multiplied_basin_size(heightmap: list, number_of_basins_to_multiply: int) -> int:
    lowest_points = get_lowest_points(heightmap)
    basins = get_basin_sizes(lowest_points, heightmap)
    basins.sort(reverse=True)
    print(f'Found basins with sizes (sorted) {basins}')
    value = 1
    for i in range(number_of_basins_to_multiply):
        value *= basins[i]
    return value

# tests
def test_display():
    f = open('day9_test_input.txt', 'r')
    lines = f.readlines()

    heightmap = prepare_data(lines)
    risk_level = get_risk_level(heightmap)
    assert risk_level == 15, 'should be 15'

    basin_size = get_multiplied_basin_size(heightmap, 3)
    assert basin_size == 1134, 'should be 1134'

f = open('day9_input.txt', 'r')
lines = f.readlines()
heightmap = prepare_data(lines)

# part 1
risk_level = get_risk_level(heightmap)
print(f'Result for part 1 is {risk_level}')

# part 2
basin_size = get_multiplied_basin_size(heightmap, 3)
print(f'Result for part 2 is {basin_size}')