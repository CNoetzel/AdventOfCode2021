def calculate_amount_of_fishs(fishs, days_to_simulate):
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
    return calculate_amount_of_fishs(new_fish_list, days_to_simulate)

# tests
def test_fish_reproduction():
    test_fish_data = [3,4,3,1,2]

    amount_of_fishs = calculate_amount_of_fishs(test_fish_data, 18)
    assert amount_of_fishs == 26, 'should be 26'

    #overlaps_conplex = get_overlapping_lines(test_vent_data, 2, True)
    #assert overlaps_conplex == 12, 'should be 12'

f = open('day6_input.txt', 'r')
lines = f.readlines()
fish_data = list(map(int,lines[0].strip().split(',')))
amount_of_fishs = calculate_amount_of_fishs(fish_data, 80)
print(f'Result for part 1 is {amount_of_fishs}')

