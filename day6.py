# This function wa used for part one but its pretty inperformant for part 2
def calculate_amount_of_fishs_simple(fishs: list, days_to_simulate: int):
    new_fish_list = []
    for fish in fishs:
        # spawn new fish
        if fish == 0:
            new_fish_list.append(6)
            new_fish_list.append(8)
        else:
            new_fish_list.append(fish-1)
    days_to_simulate -= 1
    if days_to_simulate == 0: return len(new_fish_list)
    return calculate_amount_of_fishs_simple(new_fish_list, days_to_simulate)

def init_fish_reproduction_list(fishs: list):
    fish_reproduction_list = [0 for i in range(9)]
    for fish in fishs:
        fish_reproduction_list[fish] += 1
    return fish_reproduction_list

# This functions is a better approach to calculate the number of fishs
# they won't be handled individually instead we count the number of fishs in each state
def calculate_amount_of_fishs_optimized(reproduction_list: list, days_to_simulate: int):
    # if no more days to simulate count fishs
    if days_to_simulate == 0:
        count = 0
        for entry in reproduction_list:
            count += entry
        return count

    # otherwise adapt list
    new_list = [0 for i in range(9)]
    reproduction_candidates = reproduction_list[0]  # fishs in index will reproduce
    for day in range(1, 9):
        new_list[day-1] = reproduction_list[day]
    new_list[8] = reproduction_candidates # each fish will produce a new other fish
    new_list[6] += reproduction_candidates # after reproduction fish have to wait 6 days again

    days_to_simulate -= 1
    return calculate_amount_of_fishs_optimized(new_list, days_to_simulate)

# tests
def test_fish_reproduction():
    test_fish_data = [3,4,3,1,2]

    amount_of_fishs = calculate_amount_of_fishs_simple(test_fish_data, 18)
    assert amount_of_fishs == 26, 'should be 26'

    rep_list = init_fish_reproduction_list(test_fish_data)
    amount_of_fishs_calculated = calculate_amount_of_fishs_optimized(rep_list, 18)
    assert amount_of_fishs_calculated == 26, 'should be 26'

    rep_list = init_fish_reproduction_list(test_fish_data)
    amount_of_immortal_fishs = calculate_amount_of_fishs_optimized(rep_list, 256)
    assert amount_of_immortal_fishs == 26984457539, 'should be 26984457539'

def main():
    f = open('day6_input.txt', 'r')
    lines = f.readlines()
    fish_data = list(map(int,lines[0].strip().split(',')))

    # part 1
    amount_of_fishs = calculate_amount_of_fishs_simple(fish_data, 80)
    print(f'Result for part 1 is {amount_of_fishs}')

    # part 2
    reproduction_list = init_fish_reproduction_list(fish_data)
    amount_of_fishs = calculate_amount_of_fishs_optimized(reproduction_list, 256)
    print(f'Result for part 2 is {amount_of_fishs}')

if __name__ == "__main__":
    main()