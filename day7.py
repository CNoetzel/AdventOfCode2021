def calculate_minimum_spent_fuel(crab_positions: list):
    min_pos = min(crab_positions)
    max_pos = max(crab_positions)

    min_fuel_spent = None
    optimal_position = None
    for pos in range(min_pos, max_pos):
        fuel_spent = 0
        for crab_pos in crab_positions:
            fuel_spent += abs(crab_pos - pos)
        if min_fuel_spent == None or min_fuel_spent > fuel_spent:
            min_fuel_spent = fuel_spent
            optimal_position = pos
    
    print(f'Optimal position found at {optimal_position} with fuel spent {min_fuel_spent}')
    return min_fuel_spent

def test_fish_reproduction():
    test_crab_data = [16,1,2,0,4,2,7,1,2,14]

    minmum_spent_fuel = calculate_minimum_spent_fuel(test_crab_data)
    assert minmum_spent_fuel == 37, 'should be 37'

f = open('day7_input.txt', 'r')
lines = f.readlines()
crab_data = list(map(int,lines[0].strip().split(',')))

# part 1
minmum_spent_fuel = calculate_minimum_spent_fuel(crab_data)
print(f'Result for part 1 is {minmum_spent_fuel}')