from typing import Set

class Coordinate:
    def __init__(self, x, y): 
        self.x: int = x
        self.y: int = y
        self.count: int = 1
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self.x) + hash(self.y)
    
    def __repr__(self):
        return f'{self.x}/{self.y} count: {self.count}'

class Coorinate_Store:
    def __init__(self): 
        self.set: Set[Coordinate] = set()
    
    def add_coordinate(self, coord_to_add: Coordinate):
        if coord_to_add in self.set:
            v_coords = [c for c in self.set if c==coord_to_add]
            v_coords[0].count +=1
        else:
            self.set.add(coord_to_add)

def calculate_visited_coordinates(source: Coordinate, destination: Coordinate, 
visited_coordinates: Coorinate_Store, consider_diagonal_lines: bool):
    if source.x == destination.x: # if x1 = x2 -> vertical move
        smallest_y = min(source.y, destination.y)
        highest_y = max(source.y, destination.y)
        for y in range(smallest_y, highest_y + 1):
            visited_coordinates.add_coordinate(Coordinate(source.x, y))
    elif source.y == destination.y: # if y1 = y2 -> horizonal move
        smallest_x = min(source.x, destination.x)
        highest_x = max(source.x, destination.x)
        for x in range(smallest_x, highest_x + 1):
            visited_coordinates.add_coordinate(Coordinate(x, source.y))
    elif consider_diagonal_lines: # diagonal move
        # always start at source and decide based on data to increment or decremt position by 1
        y_counter = source.y
        increment_x = 1 if source.x < destination.x else -1
        increment_y = 1 if source.y < destination.y else -1
        for x in range(source.x, destination.x + increment_x, increment_x):
            visited_coordinates.add_coordinate(Coordinate(x, y_counter))
            y_counter += increment_y

def get_overlapping_lines(vent_data, minium_overlap_amount, consider_diagonal_lines):
    visited_coordinates = Coorinate_Store()
    
    # Loop through all lines and count overlaps
    for line_segment in vent_data:
        coords = str(line_segment).strip().split(" -> ")
        from_data = str(coords[0]).strip().split(",")
        to_data = str(coords[1]).strip().split(",")
        source = Coordinate(int(from_data[0]), int(from_data[1]))
        destination = Coordinate(int(to_data[0]), int(to_data[1]))
        calculate_visited_coordinates(source, destination, visited_coordinates, consider_diagonal_lines)

    # Count number of overlaps
    counter = 0
    for coordinate in visited_coordinates.set:
        if coordinate.count >= minium_overlap_amount: counter += 1 

    return counter
    
# tests
def test_overlapping_analytics():
    f = open('day5_test_input.txt', 'r')
    test_vent_data = f.readlines()

    overlaps_simple = get_overlapping_lines(test_vent_data, 2, False)
    assert overlaps_simple == 5, 'should be 5'

    overlaps_conplex = get_overlapping_lines(test_vent_data, 2, True)
    assert overlaps_conplex == 12, 'should be 12'

f = open('day5_input.txt', 'r')
vent_data = f.readlines()

# part 1
overlaps_part_1 = get_overlapping_lines(vent_data, 2, False)
print(f'Result for part 1 is {overlaps_part_1}')

# part 2
overlaps_part_2 = get_overlapping_lines(vent_data, 2, True)
print(f'Result for part 2 is {overlaps_part_2}')
