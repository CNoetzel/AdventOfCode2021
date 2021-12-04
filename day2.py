# navigate accoring to a list of given commands
def navigate(commands):
    horizontal = 0
    depth = 0
    
    for command in commands:
        tokens = command.split(' ')
        if tokens[0] == 'forward':
            horizontal += int(tokens[1])
        elif tokens[0] == 'down':
            depth += int(tokens[1])
        elif tokens[0] == 'up':
            depth -= int(tokens[1])
            
    return {'horizontal': horizontal, 'depth': depth}

# navigate accoring to a list of given commands with aim
def navigate_with_aim(commands):
    horizontal = 0
    depth = 0
    aim = 0
    
    for command in commands:
        tokens = command.split(' ')
        if tokens[0] == 'forward':
            horizontal += int(tokens[1])
            depth += aim * int(tokens[1])
        elif tokens[0] == 'down':
            aim += int(tokens[1])
        elif tokens[0] == 'up':
            aim -= int(tokens[1])
            
    return {'horizontal': horizontal, 'depth': depth}

# tests
def test_navigation():
    test_commands = ['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']
    position = navigate(test_commands)
    assert position['horizontal'] * position['depth'] == 150, 'should be 150'
    position = navigate_with_aim(test_commands)
    assert position['horizontal'] * position['depth'] == 900, 'should be 90'

f = open('day2_input.txt', 'r')
commands = f.readlines()

# part 1
position = navigate(commands)
result = position['horizontal'] * position['depth']
print(f'Result for part 1 is {result}')

# part 2
position = navigate_with_aim(commands)
result = position['horizontal'] * position['depth']
print(f'Result for part 2 is {result}')