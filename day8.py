class Seven_Segment_Display:
    #  + 1 +    Each segment has a number (id),
    # +     +   if we add the numbers of
    # 2     3   active segments each digit
    # +     +   has a specific sum:
    #  + 4 +    0=24   5=19
    # +     +   1=8    6=25
    # 6     5   2=21   7=9
    # +     +   3=20   8=28
    #  + 7 +    4=14   9=22

    def __init__(self):
        self.segmentMap = {
            'a': None,
            'b': None,
            'c': None,
            'd': None,
            'e': None,
            'f': None,
            'g': None
        }
        self.sumDigitMap = {
            24: 0,
            8: 1,
            21: 2,
            20: 3,
            14: 4,
            19: 5,
            25: 6,
            9: 7,
            28: 8,
            22: 9
        }
    
    def retrieve_pattern_of_size(self, patterns: list, size: int):
        found = []
        for pattern in patterns:
            if len(pattern) == size:
                found.append(pattern)
        return found

    def initialize_display(self, signalPattern: str):
        splitted_pattern = signalPattern.strip().split(' ')
        splitted_pattern.sort(key=str.__len__)

        # retrieve unique input signals
        one = splitted_pattern[0]
        seven = splitted_pattern[1]
        four = splitted_pattern[2]
        eight = splitted_pattern[len(splitted_pattern)-1]
        five_segs = self.retrieve_pattern_of_size(splitted_pattern, 5)
        six_segs = self.retrieve_pattern_of_size(splitted_pattern, 6)
        known_signals = []
        
        # in position 0 and 1 we have patterns for digits 1 and 7, 
        # so we know which signal triggers segment with id 1
        signal_1 = set(seven)
        trigger = signal_1.difference(one).pop()
        self.segmentMap[trigger] = 1
        known_signals.append(trigger)

        # the digits with 5 segments have the segment with id 1,4,7 in common
        singal_1_4_7 = set(five_segs[0]).intersection(five_segs[1]).intersection(five_segs[2])
        signal_7 = singal_1_4_7.difference(four).difference(seven).pop()
        self.segmentMap[signal_7] = 7
        known_signals.append(signal_7)

        # as 1 and 7 are known now we also know trigger for segment 4
        signal_4 = singal_1_4_7.difference(known_signals).pop()
        self.segmentMap[signal_4] = 4
        known_signals.append(signal_4)

        # get trigger for segment 2
        signal_2 = set(four).difference(seven).difference(known_signals).pop()
        self.segmentMap[signal_2] = 2
        known_signals.append(signal_2)

        # get trigger for segment 6
        signal_6 = set(eight).difference(four).difference(known_signals).pop()
        self.segmentMap[signal_6] = 6
        known_signals.append(signal_6)

        # for the digits with 6 segments we have to analyse wich input is which digit
        digit_6 = [x for x in set(six_segs) 
        if self.get_input_for_segment(6) in str(x) and 
        self.get_input_for_segment(4) in str(x)]
        signal_3 = set(eight).difference(digit_6[0]).pop()
        self.segmentMap[signal_3] = 3
        known_signals.append(signal_3)

        # the remaining segment 5 is easy now
        signal_5 = set(one).difference(known_signals).pop()
        self.segmentMap[signal_5] = 5
        known_signals.append(signal_5)

        #print(f'Known: {known_signals} Map: {self.segmentMap}')
        return

    def get_input_for_segment(self, segment: int):
        for key in self.segmentMap.keys():
            if self.segmentMap[key] == segment: return key

    def get_digit(self, input: str):
        sum = 0
        for key in input:
            sum += self.segmentMap[key]
        return self.sumDigitMap[sum]


# simple function for part 1 to count the unique output numbers
def get_unique_numbers(input: list):
    unique_numbers = 0
    unique_output = [2,3,4,7]
    for line in input:
        splitted_data = str(line).strip().split(' | ')
        output_values = splitted_data[1]
        for output in output_values.split(' '):
            if len(output) in unique_output:
                unique_numbers += 1
    return unique_numbers

# function to initialize the display concat the digits and add them
# magic is done in the display class
def get_sum_of_output(input: list):
    sum = 0
    for line in input:
        display = Seven_Segment_Display()
        splitted_data = str(line).strip().split(' | ')
        signal_data = splitted_data[0]
        output_values = splitted_data[1]
        display.initialize_display(signal_data)
        number = ''
        for digit_signal in output_values.split(' '):
            number += str((display.get_digit(digit_signal)))
        print(f'Digit: {number}')
        sum += int(number)
    return sum

# tests
def test_display():
    f = open('day8_test_input.txt', 'r')
    lines = f.readlines()

    unique_numbers = get_unique_numbers(lines)
    assert unique_numbers == 26, 'should be 26'

    sum_of_output = get_sum_of_output(lines)
    assert sum_of_output == 61229, 'should be 61229'

def main():
    f = open('day8_input.txt', 'r')
    lines = f.readlines()

    # part 1
    unique_numbers = get_unique_numbers(lines)
    print(f'Result for part 1 is {unique_numbers}')

    # part 2
    sum_of_output = get_sum_of_output(lines)
    print(f'Result for part 2 is {sum_of_output}')

if __name__ == "__main__":
    main()