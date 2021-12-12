# calculate depth by comparing with preceeding value
def calculate_depth_increase(measurements):
    previous_measurement = int(measurements[0])
    measure_increase_count = 0
    for line in measurements:
        current_value = int(line)
        if previous_measurement < current_value:
            measure_increase_count += 1
        previous_measurement = current_value
    return measure_increase_count

# calculate depth by comparing with preceeding group of values
def calculate_depth_increase_with_sliding_window(measurements, window_size):
    measure_increase_count = 0
    previous_window = calculate_window_sum(0, window_size, measurements)
    for i in range(0, len(measurements)):
        currentWindow = calculate_window_sum(i, window_size, measurements)
        if previous_window < currentWindow:
            measure_increase_count += 1
        previous_window = currentWindow
    return measure_increase_count

# function to sum up values for a group with a given window size
def calculate_window_sum(index, window_size, measurements):
    sum = 0
    for i in range(index, index + window_size):
        if(i < len(measurements)):
            sum += int(measurements[i])
    return sum

# tests
def test_calculation():
    test_measurements = [199,200,208,210,200,207,240,269,260,263]
    assert calculate_depth_increase(test_measurements) == 7, 'Should be 7'
    assert calculate_depth_increase_with_sliding_window(test_measurements, 3) == 5, 'Should be 5'

def main():
    file = open("day1_input.txt", "r")
    measurements = file.readlines()

    # part 1
    result = calculate_depth_increase(measurements)
    print(f'Result for part 1 is {result}')

    # part 2
    result = calculate_depth_increase_with_sliding_window(measurements, 3)
    print(f'Result for part 2 is {result}')

if __name__ == "__main__":
    main()