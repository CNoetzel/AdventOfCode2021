from enum import Enum

class Significance(Enum):
    MOST = 1,
    LEAST = 0

def get_stripped_length(line):
    return len(str(line).strip())

def calculate_rates(diagnostic_input):
    # build a array for counting zeros
    # array is initialized with zeros depending on the length of the first line
    zero_counter = [0 for i in range(get_stripped_length(diagnostic_input[0]))]
    
    # count zeros by iterating through the input
    for binary in diagnostic_input:
        for i in range(0, get_stripped_length(binary)):
            if int(binary[i]) == 0: zero_counter[i] += 1

    gamma_rate = ''
    epsilon_rate = ''

    # if our counted zeros has a value greater than the half of all line
    # the zero is the most common bit otherwise its the one
    threshold = len(diagnostic_input)/2
    for count in zero_counter:
        gamma_rate += '0' if count > threshold else '1'
        epsilon_rate += '1' if count > threshold else '0'
    
    print(f'Gamma rate is: {gamma_rate} and epsilon rate is: {epsilon_rate}')

    return {
        'gamma_rate': int(gamma_rate, 2),
        'epsilon_rate': int(epsilon_rate, 2)
    }

def calculate_rate_recursive(index, diagnostic_input, significance):
    # abort if only one element is left in array
    if len(diagnostic_input) == 1: return diagnostic_input[0]
    
    zero_counter = 0
    # count zeros on position "index"
    for binary in diagnostic_input:
        if int(binary[index]) == 0: zero_counter += 1

    # create new input based on significane
    threshold = len(diagnostic_input)/2
    new_diagnostic_input = []
    
    value_to_keep = None
    if zero_counter == threshold:
        value_to_keep = 0 if significance == Significance.LEAST else 1
    elif (zero_counter > threshold and significance == Significance.MOST) or \
         (zero_counter < threshold and significance == Significance.LEAST): 
        value_to_keep = 0
    else:
        value_to_keep = 1
        
    for binary in diagnostic_input:
        if int(binary[index]) == value_to_keep:
            new_diagnostic_input.append(binary)

    # recursive call
    new_index = index + 1
    return calculate_rate_recursive(new_index, new_diagnostic_input, significance)

# calculate power consumption based on input
def calculate_power_consumption(diagnosic_input):
    rates = calculate_rates(diagnosic_input)
    return rates['gamma_rate'] * rates['epsilon_rate']

def calculate_life_rating_support(diagnosic_input):
    oxygen = calculate_rate_recursive(0, diagnosic_input, Significance.MOST)
    carbon = calculate_rate_recursive(0, diagnosic_input, Significance.LEAST)
    return int(oxygen, 2) * int(carbon, 2)

# tests
def test_diagnostics():
    f = open('day3_test_input.txt', 'r')
    test_diagnostic_report = f.readlines()
    power_consumption = calculate_power_consumption(test_diagnostic_report)
    assert power_consumption == 198, 'should be 198'

    life_rating_support = calculate_life_rating_support(test_diagnostic_report)
    assert life_rating_support == 230, 'should be 230'

def main():
    f = open('day3_input.txt', 'r')
    diagnostic_report = f.readlines()

    # part 1
    result = calculate_power_consumption(diagnostic_report)
    print(f'Result for part 1 is {result}')

    # part 2
    result = calculate_life_rating_support(diagnostic_report)
    print(f'Result for part 2 is {result}')

if __name__ == "__main__":
    main()